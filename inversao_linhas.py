import Imagem

dados = Imagem.getMatrizImagemColorida("paisagem_lago.jpg")
matriz_r = dados[0]
matriz_g = dados[1]
matriz_b = dados[2]

lin = len(matriz_b)
col = len(matriz_b[0])
print(f"Dimensao: {col} X {lin}")