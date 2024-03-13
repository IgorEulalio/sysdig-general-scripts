# Service Account Expiration Checker

This script is designed to help customers track expiration of service accounts by fetching all SAs and grouping them in expiration buckets for 30, 60 and 90 days.

## Features

- Fetches and lists all service accounts from a specified API.
- Categorizes service accounts based on their expiration dates.
- Supports environment variables for API URL and secure API token.

## Prerequisites

Before you run this script, ensure you have the following:

- Python 3.x installed on your system.
- API token should have admin access so it can list SAs for all teams.

- An API URL and a secure API token set as environment variables (`API_URL` and `SECURE_API_TOKEN`, respectively).

## Usage

1. Set the environment variables `API_URL` and `SECURE_API_TOKEN` with your API URL and secure API token.

   ```bash
   export API_URL="your_api_url_here"
   export SECURE_API_TOKEN="your_secure_api_token_here"
   ```
2. Download code dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Run the script using Python:

   ```bash
   python3 main.py
   ```

## How It Works

- The script first fetches a list of teams from the provided API URL using the secure API token.
- For each team, it then fetches the service accounts associated with that team.
- Each service account's expiration date is checked, and the account is categorized as expiring within 30, 60, or 90 days.
- The script outputs lists of service accounts categorized by their expiration periods.


