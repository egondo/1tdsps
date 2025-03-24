import Imagem

pedra = Imagem.getMatrizImagemCinza('rotacao.png')

lin = len(pedra)
col = len(pedra[0])

rotacao = []
for i in range(col):
    rotacao.append([0] * lin)

k = lin - 1
for i in range(lin):
    for j in range(col):
        rotacao[j][k] = pedra[i][j]
    k = k - 1

Imagem.salvaImagemCinza("rotacao180.png", rotacao)
print("Imagem rotacionada com sucesso!")
