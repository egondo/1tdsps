if __name__ == "__main__":
    with open('/tmp/saida.txt', mode="r") as arq:
        lista = arq.read()
        
    print(lista)
