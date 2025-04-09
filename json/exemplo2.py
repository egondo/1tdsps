import json

arq = open("json/dados.json", mode="r", encoding="utf8")
pessoa = json.load(arq)
print(pessoa)
pessoa['cpf'] = "234.928.083-77"
print(pessoa)