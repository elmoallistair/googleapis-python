from google.cloud import storage
import os

source_bucket = "elmo_test"
source_blob = "upload/upload.txt"
des_bucket = "elmo_test2"
des_blob = "files/file_copy.txt"

client = storage.Client()
bucket = client.bucket(source_bucket)
blob = bucket.blob(source_blob)
destination = client.bucket(des_bucket)

print("Copying '{}' from '{}' to '{}'...".format(
    os.path.basename(source_blob), source_bucket, des_bucket))
new_blob = bucket.copy_blob(blob, destination, des_blob)