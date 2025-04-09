import Imagem

dados = Imagem.getMatrizImagemCinza("domino.png")
lin = len(dados)
col = len(dados[0])

#print(f"{col} x {lin}")
pedra = []
for i in range(38):
    pedra.append([0] * 65)

for i in range(38):
    for j in range(65):
        pedra[i][j] = dados[i + 54][j + 15]

Imagem.salvaImagemCinza("pedra.png", pedra)  
print("Imagem gerada com sucesso!")      