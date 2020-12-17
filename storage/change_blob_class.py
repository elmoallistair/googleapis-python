from google.cloud import storage
from google.cloud.storage import constants

bucket_name = "elmo_test"
blob_name = "files/file.txt"
new_class = "NEARLINE" # https://cloud.google.com/storage/docs/storage-classes

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.get_blob(blob_name)

print("Updating '{}' storage class from {} to {}..".format(
            blob_name, blob.storage_class, new_class), end=" ")
blob.update_storage_class(new_class)
print("Done")
