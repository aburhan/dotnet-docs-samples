import os
import json
from google.cloud import bigquery

def fetch_data():
    # Load credentials from environment
    credentials_json = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    if not credentials_json:
        raise ValueError('The GOOGLE_APPLICATION_CREDENTIALS environment variable was not set.')

    # Parse credentials
    credentials = json.loads(credentials_json)

    # Create a BigQuery client
    client = bigquery.Client.from_service_account_info(credentials)

    # Define the query
    query = "SELECT * FROM `github-action-393418.test.test`"

    # Run the query
    query_job = client.query(query)

    # Print the results
    for row in query_job:
        print(dict(row))

if __name__ == '__main__':
    fetch_data()
