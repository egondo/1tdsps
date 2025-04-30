import banco
import traceback

def cadastra_pessoa(pes: dict, end: dict):
    try:
        banco.insere_pessoa(pes)
        end['id_pessoa'] = pes['id']
        banco.insere_endereco(end)

    except Exception as erro:
        traceback.print_exc() #para imprimir o stack de erro
        raise Exception("erro cadastrando a pessoa")
