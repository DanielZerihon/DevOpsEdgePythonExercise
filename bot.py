import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from details_library.csv_module import CSVManager

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

required_vars = ['SLACK_TOKEN', 'aws_access_key_id', 'aws_secret_access_key', 'SIGNING_SECRET']
missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    print(f"Error: Missing environment variables: {', '.join(missing_vars)}")
    exit(1)

app = Flask(__name__)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# Initialize the CSV Manager with S3 details
manager = CSVManager(
    aws_access_key_id=os.environ['aws_access_key_id'],
    aws_secret_access_key=os.environ['aws_secret_access_key'],
    bucket_name="devopsedge-s3-bucket-for-excersice",
    file_key="user3.csv"
)

@app.route('/download', methods=['POST'])
def download_csv():
    """Return the PhoneBook CSV file as an attachment."""
    data = request.form
    print(data)
    channel_id = data.get('channel_id')
    try:
        if not os.path.exists(manager.file_key):
            manager.download_csv()
        print(f"file_path {manager.file_key}")
        client.files_upload_v2(
            channels=channel_id,
            file=manager.file_key,
            title="PhoneBook CSV",
            initial_comment="Here is the PhoneBook CSV file."
        )
        response_text = "CSV file uploaded successfully."
    except Exception as e:
        response_text = f"Error downloading CSV: {e}"

    client.chat_postMessage(channel=channel_id, text=response_text)
    return Response(), 200

@app.route('/get', methods=['POST'])
def get_record():
    """Retrieve a record by name."""
    data = request.form
    text = data.get('text', '').strip()
    channel_id = data.get('channel_id')
    record = manager.retrieve_record(text)
    if record:
        response_text = f"Record found: {record}"
    else:
        response_text = f"No record found for name: {text}"

    client.chat_postMessage(channel=channel_id, text=response_text)
    return Response(), 200

@app.route('/add', methods=['POST'])
def add_record():
    """Add a new record to the CSV file."""
    data = request.form
    text = data.get('text', '')
    channel_id = data.get('channel_id')

    try:
        print(f"text before split == {text}")
        name, phone, email = text.split(',')
        print(f"name, phone, email == {name}, {phone}, {email}")
        manager.add_record(name.strip(), phone.strip(), email.strip())
        response_text = f"Record added: Name={name}, Phone={phone}, Email={email}"
    except ValueError:
        response_text = "Invalid input format. Use: /add <name>,<phone>,<email>"
    except Exception as e:
        response_text = f"Error adding record: {e}"

    client.chat_postMessage(channel=channel_id, text=response_text)
    return Response(), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)