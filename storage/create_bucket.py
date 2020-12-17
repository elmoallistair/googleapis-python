from google.cloud import storage

bucket_name = "elmo_test"

client = storage.Client()
bucket = client.bucket(bucket_name)

bucket.storage_class = "STANDARD"
bucket.location = "US"

print("Creating bucket '{}' in location '{}'...".format(
    bucket_name, bucket.location), end=" ")
client.create_bucket(bucket)
print("Done")