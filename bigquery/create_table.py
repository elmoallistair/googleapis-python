# Create a table

from google.cloud import bigquery

client = bigquery.Client()

schema = [
    bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
]

table_id = "<PROJECT>.<DATASET>.<TABLE>"

table = bigquery.Table(table_id, schema=schema)

new_table = client.create_table(
    table=table,
    exists_ok=False,
    timeout=30
)