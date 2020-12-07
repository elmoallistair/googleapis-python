# Import library
from google.cloud import bigquery

# Initialize a BigQuery client object
client = bigquery.Client()

# Set dataset ID
dataset_name = "playground"
dataset_id = "{}.{}".format(client.project, dataset_name)

# Construct dataset object
dataset = bigquery.Dataset(dataset_id)

# Set dataset location
dataset.location = "US"

# API call: create the dataset via a POST request
dataset = client.create_dataset(dataset, timeout=30)
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
