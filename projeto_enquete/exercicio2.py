import banco
import datetime

perguntas = banco.recupera_perguntas()

respondente = input("Quem é vc?")

respostas = []
aux = datetime.datetime.now()
hoje = aux.strftime('%x')
print(hoje)
for perg in perguntas:
    s = f"{perg[1]}) {perg[2]}\n"
    resp = input(s)

    info_resp = {
        "respondente": respondente,
        "valor": resp,
        'id_pergunta': perg[0],
        'data': hoje
    }
    respostas.append(info_resp)

for resp in respostas:
    banco.insere_resposta(resp)