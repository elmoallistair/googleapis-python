from google.cloud import storage

bucket_name = "elmo_test3"

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)

# note: bucket must be empty for deleting
print("Deleting bucket '{}'...".format(bucket.name), end=" ")
bucket.delete()
print("Done")
