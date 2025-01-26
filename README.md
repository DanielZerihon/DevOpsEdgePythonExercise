# DevOpsEdgePythonExercise

This repository demonstrates the implementation of a Flask-based bot that interacts with Slack and allows the management of CSV files stored in AWS S3. It includes a set of scripts and configuration files for packaging and deploying the bot into a containerized environment using Docker.

## Overview
The bot allows the following functionalities:
1. **Download CSV**: Download a CSV file stored in AWS S3 and upload it to a Slack channel.
2. **Get Record**: Retrieve a specific record from the CSV file by name.
3. **Add Record**: Add a new record to the CSV file with name, phone number, and email.

It uses `Flask` to set up a simple web server with routes for the above functionalities. 
Environment variables are used for configuration, and dependencies are managed through `requirements.txt`.

## Features
- Interacts with Slack using the `slack-sdk`.
- Uses AWS S3 for storing and retrieving CSV files.
- Allows adding and retrieving records from the CSV file.
- Dockerized for easy deployment.
- Includes build files for packaging the Python application.
- Uses a CLI to the Python library so the command can be executed from the terminal as a command line.

## Directory Structure

├── 

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd DevOpsEdgePythonExercise
   ```

2. Define the environment variables in the `.env` file, as the following:
   ```
   SLACK_TOKEN=<your_slack_token>
   aws_access_key_id=<your_aws_access_key_id>
   aws_secret_access_key=<your_aws_secret_access_key>
   SIGNING_SECRET=<your_slack_signing_secret>
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Build the Python package using `pyproject.toml` and `setuptools`:
   ```bash
   python -m build
   ```

## How to Use
### Docker Build and Run
1. Build the Docker image:
   ```bash
   docker build -t slack-bot .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 --env-file .env slack-bot
   ```

3. The bot will be available at `http://localhost:5000` and you can interact with it via Slack.

### Flask Routes
- **/download**: Uploads the CSV file from AWS S3 to a Slack channel.
  - Method: POST
  - Parameters: `channel_id`

- **/get**: Retrieves a specific record from the CSV file.
  - Method: POST
  - Parameters: `text` (record name), `channel_id`

- **/add**: Adds a new record to the CSV file.
  - Method: POST
  - Parameters: `text` (format: `<name>,<phone>,<email>`), `channel_id`

## Build and Run
To build and run the bot as a containerized application:

1. Build the Docker image:
   ```bash
   docker build -t slack-bot .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 --env-file .env slack-bot
   ```

3. Visit `http://localhost:5000` to interact with the bot via Slack.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
