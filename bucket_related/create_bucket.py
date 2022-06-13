
import os
from google.cloud import storage

if __name__ == "__main__":
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"D:\Google Cloud Data\radiant-saga-351413-457e57ce1bc8.json"
    storage_client = storage.Client()
    bucket = storage_client.bucket("bucket_client_pycharm")
    bucket.storage_class = "STANDARD"
    new_bucket = storage_client.create_bucket(bucket,location = 'US')

    print("bucket name: " +str(new_bucket.name))
    print("bucket storage class: " +str(new_bucket.storage_class))
    print("bucket location: " +str(new_bucket.location))

