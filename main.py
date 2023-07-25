import os
import subprocess
from ghapi.all import GhApi
from google.cloud import bigquery
from yaml import safe_load, safe_dump



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
