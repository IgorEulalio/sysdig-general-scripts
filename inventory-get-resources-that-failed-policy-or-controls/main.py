import csv
import requests
import sys
import os

sysdig_url = os.environ.get('API_URL')
token = os.environ.get('SECURE_API_TOKEN')


def fetch_data(zone):
    """
    Fetches data from the API.
    """
    url = f"{sysdig_url}/api/cspm/v1/inventory/graph-resources?pageNumber=1&pageSize=500&filter=policy.failed exists and zone in (\"{zone}\")&fields=id%2Chash%2Cname%2Cplatform%2Ctype%2Cmetadata%2Cposturepolicysummary%2Cresourceorigin&entities[]=kubeworkload&entities[]=kubeidentity&entities[]=host&entities[]=cluster&entities[]=awsresource&entities[]=gcpresource&entities[]=azureresource&entities[]=gitworkload&entities[]=gitcloud&entities[]=image"
    headers = {
        'Authorization': 'Bearer ' + token,
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an HTTPError if the response status code was unsuccessful
    return response.json()

def flatten_data(data):
    """
    Flattens the data dictionary into a list of values.
    """
    flattened = []
    for item in data['data']:
        # Flatten metadata
        metadata = item.pop('metadata', {})
        item.update({f'metadata_{key}': value for key, value in metadata.items()})
        
        # Flatten vulnerabilitySummary
        vulnerability_summary = item.pop('vulnerabilitySummary', {})
        item.update({f'vulnerabilitySummary_{key}': value for key, value in vulnerability_summary.items()})
        
        # Flatten inUseVulnerabilitySummary
        in_use_vulnerability_summary = item.pop('inUseVulnerabilitySummary', {})
        item.update({f'inUseVulnerabilitySummary_{key}': value for key, value in in_use_vulnerability_summary.items()})
        
        # Flatten controls
        controls = item.pop('controls', [])
        item['controls'] = ";".join([str(control) for control in controls])
        
        flattened.append(item)
    return flattened

def write_to_csv(data, filename="output.csv"):
    """
    Writes the data to a CSV file.
    """
    if data:
        keys = data[0].keys()
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

def main(zone):
    data = fetch_data(zone)
    flattened_data = flatten_data(data)
    write_to_csv(flattened_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <ZONE>")
        sys.exit(1)
    zone = sys.argv[1]
    main(zone)
