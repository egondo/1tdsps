import json

info = {
    "nome": "Joao",
    "sobrenome": "Alvares",
    "genero": "masculino",
    "idade": 35,
    "nacionalidade": "brasileira"
}

arq = open("json/dados.json", mode="w", encoding="utf8")
json.dump(info, arq, indent=4)
arq.close()

