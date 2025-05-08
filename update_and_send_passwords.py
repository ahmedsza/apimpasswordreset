import random
import string
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.apimanagement import ApiManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-apimanagement
    pip install python-dotenv
# USAGE

    python update_and_send_passwords.py

    Before running the sample, set the values in a `.env` file:
        AZURE_SUBSCRIPTION_ID=<your_subscription_id>
        AZURE_RESOURCE_GROUP=<your_resource_group_name>
        AZURE_SERVICE_NAME=<your_service_name>
        TARGET_USER_ID=<specific_user_id>
    
    Use az login to log in to Azure and set up the default subscription.
    Default subscription can be set using az account set --subscription <subscription_id>
    the code will user DefaultAzureCredential to authenticate.
"""

# Load environment variables from .env file
load_dotenv()

def main():
    # Read values from environment variables
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    resource_group_name = os.getenv("AZURE_RESOURCE_GROUP")
    service_name = os.getenv("AZURE_SERVICE_NAME")
    target_user_id = os.getenv("TARGET_USER_ID")

    # Initialize the API Management client
    client = ApiManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=subscription_id,
    )

    # Get the list of all users
    users = client.user.list_by_service(
        resource_group_name=resource_group_name,
        service_name=service_name
    )

    # Loop through each user
    for user in users:
        user_id = user.name
        # for testing only, remove the next 2 lines if you want to update all users
        if user_id != target_user_id:
            continue
        email = user.email
        print(email)
        first_name = user.first_name
        last_name = user.last_name
        password_length = 16
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
        print(f"Generated password: {password}")
        # Update the user's password (retain email, first name, and last name)
        client.user.create_or_update(
            resource_group_name=resource_group_name,
            service_name=service_name,
            user_id=user_id,
            parameters={
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "password": password  # Use the generated password
            }
        )

        # Send the confirmation password email
        client.user_confirmation_password.send(
            resource_group_name=resource_group_name,
            service_name=service_name,
            user_id=user_id
        )
        print(f"Password updated and confirmation email sent for user: {user_id} - ({email})")

if __name__ == "__main__":
    main()