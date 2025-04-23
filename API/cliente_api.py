import requests
import json

url = "https://dragonball-api.com/api/characters?page=1&limit=100"

objeto = requests.get(url)

dados = objeto.json()
print(dados)

arq = open("dragonball.json", mode="w")
json.dump(dados, arq, indent=4)
arq.close()