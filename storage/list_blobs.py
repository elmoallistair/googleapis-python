from google.cloud import storage

bucket_name = "elmo_test"

client = storage.Client()
bucket = client.bucket(bucket_name)

blobs = list(client.list_blobs(bucket))
for blob in blobs:
    print(blob.name)