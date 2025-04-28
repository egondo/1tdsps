import oracledb

def get_conexao():
    con = oracledb.connect(user="pf0313", password="professor#23",
                           dsn="oracle.fiap.com.br/orcl")
    return con

def insere_resposta(resposta: dict):
    ins = "insert into RESPOSTA(valor, respondente, data, id_pergunta) values(:valor, :respondente, to_date(:data, 'MM/DD/YY hh24:mi:ss'), :id_pergunta)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(ins, resposta)
        con.commit()


def insere_pergunta(pergunta: dict):
    ins = "insert into PERGUNTA(numero, questao) values(:numero, :questao)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(ins, pergunta)
        con.commit()
        
def recupera_perguntas():
    sql = "select id, numero, questao from PERGUNTA order by numero"
    dados = None
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            dados = cur.fetchall()
    return dados

def recupera_respostas():
    sql = "select r.respondente, p.numero, p.questao, r.valor, to_char(r.data, 'DD/MM/YYYY hh24:mi') from resposta r join pergunta p on r.id_pergunta = p.id order by r.respondente, p.numero"

    dados = None
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            dados = cur.fetchall()
    return dados