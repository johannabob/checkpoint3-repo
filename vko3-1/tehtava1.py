#hakee json-dataa ja kirjoittaa ne tiedostoon

import requests

data = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
jasoni = data.json()

jasonin_items = jasoni["items"]

with open("checkpoint.txt", "w") as tiedosto:
    for item in jasonin_items:
        tiedosto.write(item['parameter'])
        tiedosto.write("\n")


        
