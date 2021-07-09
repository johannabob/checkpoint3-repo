#Voidaan suorittaa komentoriviltä seuraavalla komennolla:
#python tehtava2.py 3

from google.cloud import storage

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("rivit", help="tulostaa annetun rivimäärän(int) verran tiedostosta", type=int)
args = parser.parse_args()

#lataa bucketista checkpoint3-bucket tiedoston checkpoint.txt
def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

#funktiokutsun sisällä buketin nimi, source blobin nimi ja kohdetiedoston nimi
download_blob("checkpoint3-bucket", "checkpoint.txt", "checkpoint1.txt")

#Tulostaa ladatusta tiedostosta komentoriviparametrinä annetun luvun 
# osoittaman määrän rivejä siten, että rivit on järjestetty 
# pienimmästä suurimpaan.

def vertailu(sanat):
    return len(sanat)

lista = []

with open("checkpoint1.txt") as tiedosto:
    for rivi in tiedosto:
        lista.append(rivi)

sortattu_lista = sorted(lista, key=vertailu , reverse=False)

for i in range(0, args.rivit):
    print(sortattu_lista[i]) 

