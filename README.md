# DevOpsEdgePythonExercise

This repository demonstrates the implementation of a Flask-based bot that interacts with Slack and allows the management of CSV files stored in AWS S3.  
It includes a set of scripts and configuration files for packaging and deploying the bot into a containerized environment using Docker.

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
- Uses a CLI for the Python library, enabling the command to be executed from the terminal as a command line.

## Directory Structure

```
├── Dockerfile
├── README.md
├── bot.py
├── requirements.txt
└── wheel
    ├── dist
    │   └── details_library-0.5.1-py3-none-any.whl
    ├── pyproject.toml
    └── src
        └── details_library
            ├── __init__.py
            ├── cli.py
            └── csv_module.py
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd DevOpsEdgePythonExercise
   ```

2. Define the environment variables in the `.env` file as follows:
   ```
   SLACK_TOKEN=<your_slack_token>
   aws_access_key_id=<your_aws_access_key_id>
   aws_secret_access_key=<your_aws_secret_access_key>
   SIGNING_SECRET=<your_slack_signing_secret>
   ```

3. Build the Docker image:
   ```bash
   docker build -t slack-bot .
   ```

4. Run the Docker container:
   ```bash
   docker run -p 5000:5000 slack-bot
   ```

5. The bot will now be available at `http://localhost:5000`.

6. Install `ngrok` on your VM.

7. Run `ngrok` on port 5000:
   ```bash
   ngrok http 5000
   ```

8. Go to the Slack API and configure the Slash Commands URL with the `ngrok` forwarding address.

9. Enjoy! 🎉

---

## BONUS - CLI Commands

You can execute the following CLI commands from the terminal as part of the Python library:
1. get in the docker container: 
```bash
sudo docker exec -it <CONTAINER_ID> bash
```
2. Run each command you like:
- `retrieve-record`
- `add-record`
- `download-csv`

### Flask Routes

- **/download**: Uploads the CSV file from AWS S3 to a Slack channel.  
  - Method: POST  

- **/get**: Retrieves a specific record from the CSV file.  
  - Method: POST  
  - Parameters: `text` (record name)

- **/add**: Adds a new record to the CSV file.  
  - Method: POST  
  - Parameters: `text` (format: `<name>,<phone>,<email>`)
