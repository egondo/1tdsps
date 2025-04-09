#Contagem das ocorrências das letras de uma String

palavra = input("Informe a string: ").upper()
contagem = {}

for letra in palavra:
    if letra != ' ':
        if letra in contagem.keys():
            contagem[letra] = contagem[letra] + 1
        else:
            contagem[letra] = 1

for chave in contagem:
    print(f'{chave} => {contagem[chave]}')