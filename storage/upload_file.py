from google.cloud import storage
import os

bucket_name = "elmo_test"
source = "res/upload.txt" # local
destination = "files/upload.txt" # bucket

client = storage.Client()
bucket = client.bucket(bucket_name)
blob = bucket.blob(destination)

print("Uploading file '{}'... to '{}'".format(
    os.path.basename(source), bucket_name))
blob.upload_from_filename(source)
print("File uploaded to 'gs://{}/{}'".format(
    bucket_name, destination))
