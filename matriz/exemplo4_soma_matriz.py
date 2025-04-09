def soma(mat_a: list, mat_b: list) -> list:
    lin_a = len(mat_a)
    col_a = len(mat_a[0])

    lin_b = len(mat_b)
    col_b = len(mat_b[0])
    if lin_a != lin_b or col_a != col_b:
        raise Exception("Impossível somar as matrizes, as dimensoes são diferentes!")

    resultado = []
    for j in range(lin_a):
        resultado.append([0] * col_a)

    for i in range(lin_a):
        for j in range(col_a):
            resultado[i][j] = mat_a[i][j] + mat_b[i][j]
    
    return resultado


if __name__ == "__main__":
    a = [
        [2, 5, -2, -6, 8],
        [-4, 6, 2, 9, 7],
        [-1, 0, 9, 3, 4]
    ]
    b = [
        [-9, 3, 5, 8],
        [0, -1, 4, 2],
        [7, -1, -5, 2]
    ]
    resultado = soma(a, b)
    for lin in resultado:
        print(lin)