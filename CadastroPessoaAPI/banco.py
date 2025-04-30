import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def insere_endereco(end: dict):
    ins = "insert into tbs_endereco(logradouro, numero, complemento, bairro, municipio, cep, id_pessoa) values(:logradouro, :numero, :complemento, :bairro, :municipio, :cep, :id_pessoa)"

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(ins, end)
        con.commit()

def insere_pessoa(pes: dict):
    ins = "insert into tbs_pessoa(nome, telefone, cpf, sexo, nascimento) values(:nome, :telefone, :cpf, :sexo, to_date(:nascimento, 'DD/MM/YYYY')) returning id into :id"

    with get_conexao() as con:
        with con.cursor() as cur:
            new_id = cur.var(oracledb.NUMBER) #criando variavel para receber id
            pes['id'] = new_id                #colocando variavel no dicionario
            cur.execute(ins, pes)
            pes['id'] = new_id.getvalue()[0]  #substituindo a variavel oracle pelo id gerado pelo banco
        con.commit()

if __name__ == "__main__":
    pes = {
        "nome": "Daniel Boaventura",
        "telefone": "(11) 77498-2933",
        "cpf": "928.840.343-76",
        "sexo": "masculino",
        "nascimento": "29/04/2000"
    }

    insere_pessoa(pes)

    end = {
        "logradouro": "Av Paulista",
        "numero": "1106",
        "bairro": "Bela Vista",
        "complemento": "4º andar",
        "cep": "04281-000",
        "municipio": "São Paulo"
    }
    end['id_pessoa'] = pes['id']
    insere_endereco(end)



