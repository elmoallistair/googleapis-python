# Import library
from google.cloud import bigquery

# Initialize a BigQuery client object
client = bigquery.Client()

# Set dataset ID
dataset_id = "elmo-gcp.playground"

# Fetch the dataset referenced by dataset_id
dataset = client.get_dataset(dataset_id)

# Listing tables in dataset
tables = list(client.list_tables(dataset))
if tables:
    print("Found {} table in {}".format(len(tables), dataset_id))
    for table in tables:
        print("\t{}".format(table.table_id))
else:
    print("Dataset {} does not contain any tables".format(dataset_id))
