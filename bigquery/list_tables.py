# List tables in the dataset

from google.cloud import bigquery

client = bigquery.Client()

dataset_id = "[PROJECT_ID].[DATASET]"

dataset = client.get_dataset(dataset_id)
tables = list(client.list_tables(dataset))

if tables:
    print("Found {} table in dataset '{}'".format(len(tables), dataset_id))
    for table in tables:
        print("\t{}".format(table.table_id))
else:
    print("Dataset {} does not contain any tables".format(dataset_id))
