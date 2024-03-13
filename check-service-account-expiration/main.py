import os
import requests
from datetime import datetime, timedelta

# Function to convert expirationDate to a readable format
def convert_expiration_date(timestamp):
    return datetime.fromtimestamp(timestamp / 1000.0)

# Function to check if the expiration date is within the given days
def is_expiring_within_days(expiration_date, days):
    return datetime.now() + timedelta(days=days) >= expiration_date

# Function to categorize service accounts based on expiration
def categorize_service_accounts(service_accounts):
    expiring_in_30 = []
    expiring_in_60 = []
    expiring_in_90 = []
    
    for account in service_accounts:
        expiration_date = convert_expiration_date(account['expirationDate'])
        if is_expiring_within_days(expiration_date, 30):
            expiring_in_30.append(account)
        elif is_expiring_within_days(expiration_date, 60):
            expiring_in_60.append(account)
        elif is_expiring_within_days(expiration_date, 90):
            expiring_in_90.append(account)
    
    return expiring_in_30, expiring_in_60, expiring_in_90

# Main function to execute the workflow
def main():
    hostname = os.getenv('API_URL')
    bearer_token = os.getenv('SECURE_API_TOKEN')
    
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    
    # Call the first API to list teams
    teams_response = requests.get(f'{hostname}/api/v3/teams', headers=headers).json()
    teams = teams_response['data']
    
    service_accounts = []
    # Iterate over each team and call the second API
    for team in teams:
        team_id = team['id']
        accounts_response = requests.get(f'{hostname}/api/serviceaccounts/team', params={'id': team_id}, headers=headers).json()
        service_accounts.extend(accounts_response['serviceAccounts'])
    
    # Categorize service accounts based on expiration
    expiring_in_30, expiring_in_60, expiring_in_90 = categorize_service_accounts(service_accounts)
    
    # Print out the service accounts
    print("Service Accounts expiring in 30 days:", expiring_in_30)
    print("Service Accounts expiring in 60 days:", expiring_in_60)
    print("Service Accounts expiring in 90 days:", expiring_in_90)

if __name__ == "__main__":
    main()