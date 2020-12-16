# Import library
from google.cloud import bigquery

# Initialize a BigQuery client object
client = bigquery.Client()

# Set dataset ID
dataset_name = "test_create_dataset"
dataset_id = "{}.{}".format(client.project, dataset_name)

# Construct dataset object
dataset = bigquery.Dataset(dataset_id)

# Set dataset location
dataset.location = "US"

# Create the dataset via a POST request
print("Creating dataset {}.{}...".format(
    client.project, dataset.dataset_id), end=" ")
dataset = client.create_dataset(dataset, timeout=30)
print("Done")