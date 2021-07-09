#hakee json-dataa ja kirjoittaa ne tiedostoon
from google.cloud import storage
import requests

data = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
jasoni = data.json()

jasonin_items = jasoni["items"]

with open("checkpoint.txt", "w") as tiedosto:
    for item in jasonin_items:
        tiedosto.write(item['parameter'])
        tiedosto.write("\n")

#luo uuden cloud storage bucketin ja tallentaa checkpoint.txt tiedoston sinne
#päivitä tarvittaessa google_application_credentials
#$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH

def luo_bucket():
    storage_client = storage.Client()
    storage_client.create_bucket("checkpoint3-bucket")

def tallenna(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)


luo_bucket()

#funktiokutsun sisällä buketin nimi, ladattava tiedosto ja kohdeblobin nimi
tallenna("checkpoint3-bucket", "checkpoint.txt", "checkpoint.txt")
        
