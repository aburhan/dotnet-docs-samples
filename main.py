
import logging
from google.cloud import bigquery
from google.oauth2 import service_account
import os


# Construct a BigQuery client object.
#client = bigquery.Client()
credentials = service_account.Credentials.from_service_account_info(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
client = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

query = f"SELECT * FROM `github-action-393418.test.test`"

query_job = client.query(query)  # Make an API request.

for row in query_job:
    # Row values can be accessed by field name or index.
    print("key={}, value={}".format(row[0], row["key"]))

logger.info('TEST')
print("PRINT TEST")
