# APIM Password Reset Tool

This tool automates the process of resetting passwords for users in Azure API Management (APIM) and sending confirmation emails.

This is sample code with no warranties or guarantees. It is meant for demonstration purposes only.

The documentation below was generated using GitHub CoPilot. It may not be entirely accurate or up to date.

## Prerequisites

- Python 3.x
- Azure subscription
- Azure CLI installed
- Required Python packages (install using `pip install -r requirements.txt`):
    - azure-identity
    - azure-mgmt-apimanagement
    - python-dotenv

## Configuration

1. Create a `.env` file in the root directory with the following variables:
```env
AZURE_SUBSCRIPTION_ID=<your_subscription_id>
AZURE_RESOURCE_GROUP=<your_resource_group_name>
AZURE_SERVICE_NAME=<your_service_name>
TARGET_USER_ID=<specific_user_id>
```

2. Log in to Azure using Azure CLI:
```bash
az login
```

3. Set your default subscription:
```bash
az account set --subscription <subscription_id>
```

## Features

- Generates secure random passwords using letters, digits, and special characters
- Updates user passwords in Azure API Management
- Sends confirmation emails to users
- Supports targeting specific users via TARGET_USER_ID
- Preserves existing user information (email, first name, last name)

## Usage
1. Create and activate a virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Run the script using:
```bash
python update_and_send_passwords.py
```

## Security Notes

- Uses DefaultAzureCredential for authentication
- Generates 16-character passwords with mixed characters
- Sends confirmation emails through Azure APIM's built-in email system

## Error Handling

The script uses Azure SDK's built-in error handling. Ensure all environment variables are properly set before running.

