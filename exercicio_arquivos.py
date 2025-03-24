import json

arq = open('data.txt', mode="r")
dados = arq.read()
#print(dados)

linhas = dados.split("\n")
#print(linhas)

acumulados = {}

for reg in linhas:
    #print(reg)
    campos = reg.split(";")
    #print(campos)
    if not campos[0] in acumulados:
        aux = campos[0]
        acumulados[aux] = float(campos[3])
    else:
        aux = campos[0]
        acumulados[aux] = acumulados[aux] + float(campos[3])

print(acumulados)

json_arq = open('valor.json', mode="w", encoding="utf8")
json.dump(acumulados, json_arq, indent=4)