# Copy table to another table

from google.cloud import bigquery

client = bigquery.Client()

source_table_id = "elmo-gcp.playground.pd_test_write_bq"
destination_table_id = "elmo-gcp.playground.pd_test_write_bq2"

job = client.copy_table(
    source_table_id, 
    destination_table_id,
    timeout=30
)

print("Table '{}' copied to '{}'".format(
    source_table_id,destination_table_id))