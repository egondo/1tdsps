import palavras_forca as bd

def esconde_palavra(word: str, chutes: str) -> str:
    resp = ""
    for letra in word:
        if letra.lower() in chutes:
            resp = resp + letra + " "
        else:
            resp = resp + "_ "
    return resp

palavra = bd.get_country()
letras_chutadas = ""
err = 0
segredo = esconde_palavra(palavra, letras_chutadas)
while '_' in segredo and err < 6:
    print(segredo)    
    print(f"erros: {err}")
    letra = input("Letra: ").lower()
    if not letra in palavra.lower():
        err = err + 1
    letras_chutadas = letras_chutadas + letra
    segredo = esconde_palavra(palavra, letras_chutadas)

if err >= 6:
    print(f"Você foi enforcado, a palavra era {palavra}")
else:
    print(f'Parabéns, vc acertou {palavra}')








letras_chutadas = 'a'
segredo = esconde_palavra("Alemanha", letras_chutadas)
print(segredo)    