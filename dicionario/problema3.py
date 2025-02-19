def busca(lista: list, cod: int) -> int:
    i = 0
    while i < len(lista) and lista[i]['codigo'] != cod:
        i = i + 1
    if i == len(lista):
        return -1
    else:
        return i

def cadastra(lista: list):
    codigo = int(input("Código do produto: "))
    if busca(lista, codigo) != -1:
        print("Código de produto existente!")
    else:
        desc = input("Descrição: ")
        qtd = int(input('Quantidade: '))
        prc = float(input('Preço unitário: '))

        prod = {'codigo': codigo, 'descricao': desc}
        prod['quantidade'] = qtd
        prod['preco'] = prc
        lista.append(prod)


def altera(lista: list):
    cod = int(input("Código: "))
    pos = busca(lista, cod)
    if pos == -1:
        print("Não existe produto especificado")
    else:
        desc = input("Descricao: ")
        qtd = int(input("Quantidade: "))
        prc = float(input("Preço: "))

        prod = lista[pos]
        prod['descricao'] = desc
        prod['quantidade'] = qtd
        prod['preco'] = prc

def consulta(lista: list) -> list:
    pass


def exclui(lista: list):
    cod = int(input("Código: "))
    pos = busca(lista, cod)
    if pos == -1:
        print("Produto não existe")
    else:
        lista.pop(pos)


def imprime(lista: list):
    for prod in lista:
        print(prod)


if __name__ == "__main__":
    lista_prod = []

    opcao = 0
    while opcao != 5:
        print('1 - cadastra')
        print('2 - altera')
        print('3 - consulta')
        print('4 - exclui')
        print('5 - sair')
        opcao = int(input("Opção: "))
        if opcao == 1:
            cadastra(lista_prod)
        elif opcao == 2:
            altera(lista_prod)
        elif opcao == 3:
            resultado = consulta(lista_prod)
            imprime(resultado)
        elif opcao == 4:
            exclui(lista_prod)
        elif opcao == 5:
            print("Obrigado por utilizar o sistema")
        else:
            print("Opção inválida!")
        
        imprime(lista_prod)