frase = "ANA E MARIANA GOSTAM DE BANANA"
pal = "ANA"

pos = frase.find(pal)
conta = 0

while pos != -1:
    conta = conta + 1
    pos = frase.find(pal, pos + 1)

print(f'O numero de vezes que {pal} aparece é {conta}')
