# List datasets for the project associated with client

from google.cloud import bigquery

client = bigquery.Client()

project_id = client.project
datasets = list(client.list_datasets())

if datasets:
    print("Found {} dataset in project '{}':".format(len(datasets), project_id))
    for dataset in datasets:
        print("\t{}".format(dataset.dataset_id))
else:
    print("Project {} does not contain any datasets".format(project_id))
