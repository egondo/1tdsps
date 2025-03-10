import json

cartas = [
    {"valor": 1, "naipe": "copas"},
    {"valor": 2, "naipe": "copas"},
    {"valor": 3, "naipe": "copas"},
    {"valor": 4, "naipe": "copas"},
    {"valor": 5, "naipe": "copas"},
    {"valor": 6, "naipe": "copas"}   
]
with open("json/baralho.txt", mode="w", encoding="utf8") as arq:
    json.dump(cartas, arq, indent=4)
