def dimensao(matriz: list) -> tuple:
    lin = len(matriz)
    col = len(matriz[0])
    return (lin, col)

def aumento(matriz: list, valor: float): 
    dim = dimensao(matriz)
    lin = dim[0] #pegando a qtd de linhas da matriz
    col = dim[1] #pegando a qtd de colunas da matriz
    for i in range(lin):
        for j in range(col):
            matriz[i][j] = matriz[i][j] + valor

if __name__ == "__main__":
    dado = [
        [1, 2, 6, 10, 23, -8],
        [0, -2, 6, 15, 20, -1],
        [4, 2, 1, 0, 10, 5]
    ]

    aumento(dado, 5)

    for lin in dado:
        print(lin)