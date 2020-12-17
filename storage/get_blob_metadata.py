from google.cloud import storage

bucket_name = "elmo_test"
blob_name = "files/file.txt"

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.get_blob(blob_name)

print("Blob: {}".format(blob.name))
print("Bucket: {}".format(blob.bucket.name))
print("Storage class: {}".format(blob.storage_class))
print("ID: {}".format(blob.id))
print("Size: {} bytes".format(blob.size))
print("Updated: {}".format(blob.updated))
print("Generation: {}".format(blob.generation))
print("Metageneration: {}".format(blob.metageneration))
print("Etag: {}".format(blob.etag))
print("Owner: {}".format(blob.owner))
print("Component count: {}".format(blob.component_count))
print("Crc32c: {}".format(blob.crc32c))
print("md5_hash: {}".format(blob.md5_hash))
print("Cache-control: {}".format(blob.cache_control))
print("Content-type: {}".format(blob.content_type))
print("Content-disposition: {}".format(blob.content_disposition))
print("Content-encoding: {}".format(blob.content_encoding))
print("Content-language: {}".format(blob.content_language))
print("Metadata: {}".format(blob.metadata))
print("Custom Time: {}".format(blob.custom_time))
print("Temporary hold: ", "enabled" if blob.temporary_hold else "disabled")
print("Event based hold: ", "enabled" if blob.event_based_hold else "disabled")