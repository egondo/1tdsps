if __name__ == "__main__":
    try:
        arq = open('/tmp/saida.txt', mode="a")
        arq.write("Bom dia\n")
        arq.write("Boa tarde!\n")
        arq.write("Testando gravacao de arquivo texto")
        arq.close()
    except:
        print("Deu erro na gravacao do arquivo")

