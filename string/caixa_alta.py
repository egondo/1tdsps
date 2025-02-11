def maiuscula(palavra: str) -> str:
    return palavra.upper()

def cria_espaco(palavra: str) -> str:
    resp = ""

    for letra in palavra:
        resp = resp + letra + " " # + indica concatenação em String 

    return resp



def substui(frase: str, letra: str) -> str:
    resp = ""
    for c in frase:
        if c == letra or c == letra.upper():
            resp = resp + '*'
        else:
            resp = resp + c
    return resp


f = "Jabuticaba"
letra = "a"
resp = substui(f, letra)
print(resp)







frase = "Hoje retornamos das férias"
resp = cria_espaco(frase)
print(resp)

