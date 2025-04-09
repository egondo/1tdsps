import banco

perguntas = [
    {"numero": 1, "questao": "Qual o seu nome?"},
    {"numero": 2, "questao": "Onde vc nasceu?"},
    {"numero": 3, "questao": "Onde vc estuda(ou)?"},
    {"numero": 4, "questao": "Qual a sua profissão?"},
    {"numero": 5, "questao": "Quais são os seus hobbies?"}
]

for quest in perguntas:
    banco.insere_pergunta(quest)