import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def insere_filme(filme: dict):
    sql = '''insert into tbl_filme(titulo, diretor, classificacao, 
    genero, duracao, lancamento, nota) values(:tit, :diretor, 
    :classif, :genero, :duracao, to_date(:data, 'DD-MM-YYYY'), 
    :nota)'''

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, filme)
        con.commit()

def consulta_filme() -> list:
    sql = "select * from tbl_filme order by lancamento desc"
    dados = None
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            dados = cur.fetchall()
    return dados

def menu_paramount() -> int:
    print("Cadastro de Filmes TI")
    print("1 - insere")
    print("2 - consulta")
    print("3 - sair")
    opcao = int(input("Informe uma opção: "))
    return opcao

if __name__ == "__main__":
    op = None
    while op != 3:
        op = menu_paramount()
        if op == 1:
            titulo = input("Título: ")
            diretor = input("Diretor: ")
            classif = input("Classificação")
            genero = input("Genero: ")
            duracao = int(input("Duração em minutos: "))
            lancamento = input("Data do lançamento (dd-mm-yyyy): ")
            nota = float(input("Nota do imdb: "))

            filme = {
                'tit': titulo, 
                'classif': classif, 
                'genero': genero,
                'diretor': diretor,
                'data': lancamento,
                'duracao': duracao,
                'nota': nota 
            }

            insere_filme(filme)
        
        elif op == 2:
            filmes = consulta_filme()
            for movie in filmes:
                print(movie)
    
    print("Encerrando o cadastro de filmes!")