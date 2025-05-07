import banco

def recupera_perguntas_enquete(enquete_id: int) -> list:
    dados = banco.recupera_perguntas(enquete_id)
    resposta = []
    entrada = None
    aux_id = -1
    for reg in dados:
        if aux_id != reg[0]: #reg[0] é o id da pergunta
            aux_id = reg[0]
            if entrada != None:
                resposta.append(entrada)
            
            entrada = { "id": reg[0], 'numero': reg[1], 'pergunta': reg[2], 
                        'tipo': reg[3], 'itens': []}
            
        if entrada['tipo'] != 'aberta':
            entrada['itens'].append(reg[4])
            
    resposta.append(entrada)
    return resposta

if __name__ == "__main__":
    dados = recupera_perguntas_enquete(1)
    for info in dados:
        print(info)                


