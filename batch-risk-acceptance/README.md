# CVE Submission Script

This script automates the submission of CVEs (Common Vulnerabilities and Exposures) to a specified API endpoint. It reads a list of CVEs from a provided text file, then sends each CVE to the Sysdig API endpoint with a payload that includes risk acceptance definitions.

## Features

- Parses a file containing a list of CVEs.
- Submits each CVE with a custom reason and expiration date.
- Utilizes environment variables for secure API token and API URL configuration.

## Requirements

- Python 3
- `requests` library

## Setup

### Virtual Environment

It is recommended to run this script within a Python virtual environment to manage dependencies.

1. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

2. **Activate the virtual environment:**

    - On Windows:

        ```cmd
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables

Set the following environment variables before running the script:

- `SECURE_API_TOKEN`: Your API token for authentication.
- `API_URL`: The base URL of your API endpoint.

For example:

```bash
export SECURE_API_TOKEN='your_secure_api_token_here'
export API_URL='https://your_api_url_here'
```

Usage

Run the script by specifying the reason, expiration date, and the path to your CVE list file as command-line arguments:
```
python3 main.py --reason RiskOwned --expirationDate 2024-02-29 --filePath cve-list.txt
```

### Arguments:
- --reason: Reason for the risk acceptance. 
- --expirationDate: Expiration date for the risk acceptance in YYYY-MM-DD format.
- --filePath: Path to the text file containing CVEs, separated by commas.

### Example
Given a file cves.txt with the following content:
```
CVE-2024-26592,CVE-2024-26594,CVE-2024-26599
```

Run the script as follows:
```
python3 main.py --reason "Accepted due to mitigating controls" --expirationDate "2024-01-02" cves.txt
```


