
if __name__ == "__main__":
    arq = open("resultados.txt", mode="r", encoding="ISO8859-1")
    dados = arq.readlines()
    
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
        
        print(f"{nome_a} = {gols_a}")
        print(f"{nome_b.strip()} = {gols_b}")

