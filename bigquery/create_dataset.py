# Create a dataset

from google.cloud import bigquery

client = bigquery.Client()

dataset_name = ""
dataset_location = ""

project_id = client.project
dataset_id = f"{project_id}.{dataset_name}"

dataset = bigquery.Dataset(dataset_id)
dataset.location = dataset_location

new_dataset = client.create_dataset(
    dataset=dataset, 
    exists_ok=False, 
    timeout=30
)