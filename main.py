
import logging
from google.cloud import bigquery

service_account_info = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
credentials = service_account.Credentials.from_service_account_info(service_account_info)
client = bigquery.Client(credentials=credentials, project=service_account_info['github-action-393418'])
# Construct a BigQuery client object.
client = bigquery.Client()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

query = f"SELECT * FROM `github-action-393418.test.test`"

query_job = client.query(query)  # Make an API request.

for row in query_job:
    # Row values can be accessed by field name or index.
    print("key={}, value={}".format(row[0], row["key"]))

logger.info('TEST')
print("PRINT TEST")
