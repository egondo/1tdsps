import Imagem


tupla = Imagem.getMatrizImagemColorida("lago_canada.jpg")
matriz_r = tupla[0]
matriz_g = tupla[1]
matriz_b = tupla[2]

lin = len(matriz_r)
col = len(matriz_r[0])

for i in range(lin):
    for j in range(col):
        matriz_r[i][j] = matriz_r[i][j] - 50
        matriz_g[i][j] = matriz_g[i][j] - 50
        matriz_b[i][j] = matriz_b[i][j] - 50

Imagem.salvaImagemColorida('lago_escuro.jpg', matriz_r, matriz_g, matriz_b)
