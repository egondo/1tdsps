def atribui_pontos_time(time: str, pontos: int, tabela: dict):
    if not time in tabela:
        tabela[time] = pontos
    else:
        valor = tabela[time]
        tabela[time] = valor + pontos


if __name__ == "__main__":
    arq = open("resultados.txt", mode="r", encoding="ISO8859-1")
    dados = arq.readlines()
    
    tab_campeonato = {}

    for linha in dados:
        campos = linha.split(" X ")
        time_a = campos[0].split(' ')
        time_b = campos[1].split(' ')
        #print(time_a)
        #print(time_b)
        if len(time_a) == 2:
            gols_a = int(time_a[1])
            nome_a = time_a[0]
        else:
            gols_a = int(time_a[2])
            nome_a = time_a[0] + " " + time_a[1] 

        gols_b = int(time_b[0])
        if len(time_b) == 2:
            nome_b = time_b[1]
        else:
            nome_b = time_b[1] + " " + time_b[2]
        
        #print(f"{nome_a} = {gols_a}")
        #print(f"{nome_b.strip()} = {gols_b}")

        if gols_a > gols_b:
            atribui_pontos_time(nome_a, 3, tab_campeonato)
            atribui_pontos_time(nome_b.strip(), 0, tab_campeonato)
            #se o nome_a estiver na tabela entao
                #somar 3 pontos para o time nome_a
            #senao
                #colocar o time nome_a no dicionario atribuindo 3pts
            
            #se o time de nome_b estiver na tabela entao
                #somar 0 pts para o time de nome_b
            #senao
                #colocar o time nome_b no dicionario atribuindo 0pts

        elif gols_a < gols_b:
            atribui_pontos_time(nome_a, 0, tab_campeonato)
            atribui_pontos_time(nome_b.strip(), 3, tab_campeonato)
            #somar 3 pontos para o time nome_b
        else:
            #somar 1 ponto para os dois times
            atribui_pontos_time(nome_a, 1, tab_campeonato)
            atribui_pontos_time(nome_b.strip(), 1, tab_campeonato)


    for chave in tab_campeonato.keys():
        print(f"{chave}: {tab_campeonato[chave]}")
