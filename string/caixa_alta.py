def maiuscula(palavra: str) -> str:
    return palavra.upper()

def cria_espaco(palavra: str) -> str:
    resp = ""

    for letra in palavra:
        resp = resp + letra + " " # + indica concatenação em String 

    return resp

frase = "Hoje retornamos das férias"
resp = cria_espaco(frase)
print(resp)

