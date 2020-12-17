from google.cloud import storage
import os

bucket_name = "elmo_test"
source = "files/upload.txt" # bucket
destination = "res/download.txt" # local

client = storage.Client()
bucket = client.bucket(bucket_name)
blob = bucket.blob(source)

print("Downloading '{}' from 'gs://{}/{}'...".format(
    os.path.basename(source), bucket_name, destination))
blob.download_to_filename(destination)
print("File saved to {}/{}".format(os.getcwd(), destination))