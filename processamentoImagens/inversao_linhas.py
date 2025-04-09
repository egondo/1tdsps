import Imagem

def inverte(mat: list):
    i = 0
    j = len(mat) - 1
    while i < j:
        aux = mat[i]
        mat[i] = mat[j]
        mat[j] = aux
        i = i + 1
        j = j - 1


dados = Imagem.getMatrizImagemColorida("paisagem_lago.jpg")
matriz_r = dados[0]
matriz_g = dados[1]
matriz_b = dados[2]

lin = len(matriz_b)
col = len(matriz_b[0])
print(f"Dimensao: {col} X {lin}")

inverte(matriz_r)
inverte(matriz_g)
inverte(matriz_b)

Imagem.salvaImagemColorida("lago_invertido.jpg", matriz_r, matriz_g, matriz_b)