def inverte(dicionario: dict) -> dict:
    dic2 = {}
    for chave in dicionario.keys():
        print(chave)
        valor = dicionario[chave]
        print(valor)
        dic2[valor] = chave
    return dic2


dic = {"truck": "caminhao", "floor": "chao"}
dic['apple'] = 'maca'
dic['pinneapple'] = 'abacaxi'
dic['car'] = 'carro'

print(dic)

outro_dic = inverte(dic)

print(outro_dic)
