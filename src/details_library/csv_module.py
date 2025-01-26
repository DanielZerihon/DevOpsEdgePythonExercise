import boto3
import os
import csv

class CSVManager:
    def __init__(self, aws_access_key_id, aws_secret_access_key, bucket_name, file_key, local_file_path="user3.csv"):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.bucket_name = bucket_name
        self.file_key = file_key
        self.local_file_path = local_file_path

    def download_csv(self):
        """Download the CSV file from S3 to the local machine."""
        try:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key
            )
            s3_client.download_file(self.bucket_name, self.file_key, self.local_file_path)
            print(f"File downloaded successfully to {self.local_file_path}")
        except Exception as e:
            print(f"Error downloading file: {e}")
            raise

    def add_record(self, name, phone, email):
        """Add a record to the CSV file."""
        try:
            # Ensure the file is downloaded
            if not os.path.exists(self.local_file_path):
                self.download_csv()

            # Append a new record to the CSV
            with open(self.local_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, phone, email])
            print("Record added successfully.")
        except Exception as e:
            print(f"Error adding record: {e}")
            raise

    def retrieve_record(self, name):
        """Retrieve a record by name."""
        try:
            # Ensure the file is downloaded
            if not os.path.exists(self.local_file_path):
                self.download_csv()

            # Search for the record
            with open(self.local_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Name"] == name:
                        return row
            print("Record not found.")
            return None
        except Exception as e:
            print(f"Error retrieving record: {e}")
            raise
