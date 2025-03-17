import velha

tab = velha.criaTabuleiro()

player = 'X'

while velha.temEspaco(tab) and not velha.haGanhador(tab):
    velha.imprime(tab)
    print(f"Vez do jogador {player}")
    lin = int(input("Linha: "))
    col = int(input("Coluna: "))
    resp = velha.joga(tab, lin, col, player)
    if resp == True:
        player = velha.trocaJogador(player)
    else:
        print("Jogada inválida, jogue novamente!")
    
player = velha.trocaJogador(player)
if velha.haGanhador(tab):
    print(f"{player} venceu!")
else:
    print("Deu velha!")