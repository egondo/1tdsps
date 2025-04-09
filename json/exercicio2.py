import json

arq = open("json/baralho.txt", mode="r", encoding="utf8")
maco = json.load(arq)
print(maco)
