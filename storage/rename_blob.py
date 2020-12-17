from google.cloud import storage
import os

bucket_name = "elmo_test"
blob_name = "files/file.txt"
new_blob_name = "files/file_rename.txt"

client = storage.Client()
bucket = client.bucket(bucket_name)
blob = bucket.blob(blob_name)

print("Renaming '{}' to '{}' in bucket '{}'...".format(
    blob_name, new_blob_name, bucket_name), end=" ")
new_blob = bucket.rename_blob(blob, new_blob_name)
print("Done")