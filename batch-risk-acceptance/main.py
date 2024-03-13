import os
import sys
import requests
import argparse
from datetime import datetime

# Parse command line arguments
parser = argparse.ArgumentParser(description="Submit CVEs with risk acceptance definitions.")
parser.add_argument("--reason", required=True, help="Reason for the risk acceptance.")
parser.add_argument("--expirationDate", required=True, help="Expiration date for the risk acceptance.")
parser.add_argument("--filePath", help="Path to the file containing CVEs, separated by commas.")
args = parser.parse_args()

# Ensure the SECURE_API_TOKEN environment variable is set
if "SECURE_API_TOKEN" not in os.environ:
    raise EnvironmentError("Missing required environment variable: SECURE_API_TOKEN")

api_url = os.environ.get("API_URL", "") + "/api/scanning/riskmanager/v2/definitions"
secure_api_token = os.environ["SECURE_API_TOKEN"]

def read_cve_file(file_path):
    with open(file_path, 'r') as file:
        cves = file.read().strip().split(',')
    return cves

def submit_cve(cve, reason, expiration_date):
    payload = {
        "riskAcceptanceDefinitions": [
            {
                "entityType": "vulnerability",
                "entityValue": cve,
                "expirationDate": expiration_date,
                "context": [],
                "reason": reason,
                "description": f"Risk acceptance in batch {datetime.now().isoformat()}"
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {secure_api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Successfully submitted {cve}")
    else:
        print(f"Failed to submit {cve}, Status Code: {response.status_code}, Response: {response.text}")

def main():
    file_path = args.filePath
    reason = args.reason
    expiration_date = args.expirationDate
    cves = read_cve_file(file_path)
    
    for cve in cves:
        submit_cve(cve, reason, expiration_date)

if __name__ == "__main__":
    main()
