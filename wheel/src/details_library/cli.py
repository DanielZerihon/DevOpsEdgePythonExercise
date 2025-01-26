import click
from details_library.csv_module import CSVManager
import os

# CLI for downloading CSV file from S3
@click.command()
@click.option('--access-key', prompt=True, help='Your AWS Access Key ID')
@click.option('--secret-key', prompt=True, help='Your AWS Secret Access Key')
@click.option('--bucket', prompt=True, help='S3 bucket name')
@click.option('--file', prompt=True, help='S3 file key')
@click.option('--local-path', default='user3.csv', help='Local path to save the CSV file')
def download_csv(access_key, secret_key, bucket, file, local_path):
    """Download CSV file from S3"""
    try:
        manager = CSVManager(access_key, secret_key, bucket, file, local_path)
        manager.download_csv()
    except Exception as e:
        print(f"Error: {e}")

# CLI for adding a record to the CSV file
@click.command()
@click.option('--access-key', prompt=True, help='Your AWS Access Key ID')
@click.option('--secret-key', prompt=True, help='Your AWS Secret Access Key')
@click.option('--bucket', prompt=True, help='S3 bucket name')
@click.option('--key', prompt=True, help='S3 file key')
@click.option('--name', prompt=True, help='Name for the record')
@click.option('--phone', prompt=True, help='Phone number for the record')
@click.option('--email', prompt=True, help='Email for the record')
@click.option('--local-path', default='user3.csv', help='Local path to save the CSV file')
def add_record(access_key, secret_key, bucket, key, name, phone, email, local_path):
    """Add a record to the CSV file"""
    try:
        manager = CSVManager(access_key, secret_key, bucket, key, local_path)
        manager.add_record(name, phone, email)
    except Exception as e:
        print(f"Error: {e}")

# CLI for retrieving a record by name
@click.command()
@click.option('--access-key', prompt=True, help='Your AWS Access Key ID')
@click.option('--secret-key', prompt=True, help='Your AWS Secret Access Key')
@click.option('--bucket', prompt=True, help='S3 bucket name')
@click.option('--key', prompt=True, help='S3 file key')
@click.option('--name', prompt=True, help='Name to search for')
@click.option('--local-path', default='user3.csv', help='Local path to save the CSV file')
def retrieve_record(access_key, secret_key, bucket, key, name, local_path):
    """Retrieve a record by name from the CSV file"""
    try:
        manager = CSVManager(access_key, secret_key, bucket, key, local_path)
        record = manager.retrieve_record(name)
        if record:
            print(f"Record: {record}")
    except Exception as e:
        print(f"Error: {e}")

# Create the CLI group and add commands
@click.group()
def cli():
    """Creating Command Line Interface for CSVManager"""
    pass

cli.add_command(download_csv)
cli.add_command(add_record)
cli.add_command(retrieve_record)

if __name__ == '__main__':
    cli()
