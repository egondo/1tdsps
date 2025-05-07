import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")


def recupera_perguntas(enquete: int) -> list:
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "select p.id, p.numero, p.questao, p.tipo, i.nome from tb_pergunta p left join tb_item i on p.id=i.pergunta_id where p.enquete_id = :id order by p.numero"

            param = {"id": enquete}

            cur.execute(sql, param)
            registros = cur.fetchall()
            return registros

if __name__ == "__main__":
    dados = recupera_perguntas(1)
    for info in dados:
        print(info)            