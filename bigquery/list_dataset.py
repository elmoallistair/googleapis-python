# Import library
from google.cloud import bigquery

# Initialize a BigQuery client object
client = bigquery.Client()

# Set Project ID for retreiving datasets
project_id = client.project

# Make an API request
# List datasets for the project associated with client
datasets = client.list_datasets()
datasets = list(datasets)

# Listing datasets
if datasets:
    print("Found {} dataset in {}".format(len(datasets), project_id))
    for dataset in datasets:
        print("\t{}".format(dataset.dataset_id))
else:
    print("Project {} does not contain any datasets".format(project_id))