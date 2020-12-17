from google.cloud import storage

project_id = "elmo-gcp"

client = storage.Client(project_id)
buckets = client.list_buckets()

print("Buckets in project '{}':".format(project_id))
for bucket in buckets:
    print(bucket.name)