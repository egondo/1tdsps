import oracledb

#abrir uma conexao com o banco de dados
conexao = oracledb.connect(user="pf0313",
                           password="professor#23",
                           dsn="oracle.fiap.com.br/orcl")

print(conexao.version)
#criando um cursor
cur = conexao.cursor()
cur.execute("SELECT * FROM TB_FILME")
registros = cur.fetchall()
for reg in registros:
    print(reg)

cur.close()
conexao.close()

#objeto conexao é equivalente ao Connection em Java
#objeto cursor é equivalente ao PreparedStatement em Java 