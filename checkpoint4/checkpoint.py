import json

def leitura_arquivo() -> list:
    try:
        with open("produtos.txt", mode="r", encoding="utf8") as arq:
            retorno = arq.readlines()
        return retorno
    except Exception as erro:
        print(erro)
        print("Arquivo não encontrado!")
        raise erro

def transforma_produto(dado: list) -> dict:
    prod = {
        "codigo": dado[0],
        "produto": dado[1],
        "quantidade": int(dado[2]),
        "preco": float(dado[3]),
        "local" : dado[4]
    }
    return prod

def cria_dicionario()-> dict:
    local_regiao = {
        "Manaus": "Norte",
        "Belém": "Norte",
        "Brasília": "Centro-Oeste",
        "Goiânia": "Centro-Oeste",
        "Cuiabá": "Centro-Oeste",
        "Campo Grande": "Centro-Oeste",
        "São Paulo": "Sudeste",
        "Rio de Janeiro": "Sudeste",
        "Vitória": "Sudeste",
        "Belo Horizonte": "Sudeste",
        "Curitiba": "Sul",
        "Porto Alegre": "Sul",
        "Florianópolis": "Sul"
    }
    return local_regiao

if __name__ == "__main__":

    registros = leitura_arquivo()
    
    registros.pop(0) #removendo a primeira linha do arquivo

    list_produtos = []
    for reg in registros:
        #dado = reg.replace('\n', '').split(';')
        reg = reg.replace('\n', '')
        dado = reg.split(";")
        prod_dic = transforma_produto(dado)
        list_produtos.append(prod_dic)

    loc_reg = cria_dicionario()
    for prod in list_produtos:
        local = prod['local']
        if local in loc_reg.keys():
            prod['regiao'] = loc_reg[local]
        else:
            prod['regiao'] = 'Nordeste'


    with open("produtos.json", mode="w", encoding="utf8") as arq:
        json.dump(list_produtos, arq, indent=4)


