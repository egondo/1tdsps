def criaTabuleiro() -> list:
    mat = []
    mat.append([' '] * 3)
    mat.append([' '] * 3)
    mat.append([' '] * 3)
    return mat

def haGanhador(mat: list) -> bool:
    for x in range(2):
        if mat[x][0] != ' ' and mat[x][0] == mat[x][1] and mat[x][1] == mat[x][2]:
            return True
        if mat[0][x] != ' ' and mat[0][x] == mat[1][x] and mat[1][x] == mat[2][x]:
            return True

    if mat[0][0] != ' ' and mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2]:
        return True

    if mat[0][2] != ' ' and mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0]:
        return True

    return False



def temEspaco(mat: list) -> bool:
    for i in range(3):
        for j in range(3):
            if mat[i][j] == ' ':
                return True
    return False




def joga(mat: list, lin: int, col: int, jogador: str) -> bool:
    if mat[lin][col] == ' ':
        mat[lin][col] = jogador
        return True
    else:
        return False



def trocaJogador(jogador:str) -> str:
    if jogador == 'X':
        return 'O'
    else:
        return 'X'





def imprime(mat: list):
    for lin in mat:
        print(lin)