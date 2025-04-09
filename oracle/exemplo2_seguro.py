import oracledb

con = oracledb.connect(user="pf0313", password="professor#23",
                       dsn="oracle.fiap.com.br/orcl")

cur = con.cursor()

modelo = input("Informe o modelo: ")
montadora = input("Montadora: ")
placa = input("Placa: ")
id = input("ID: ") #22 or 1=1

#criando sql concatenando strings
sql = f'''update tb_carro set modelo=:modelo, montadora=:montadora, 
                              placa=:placa where id=:id'''
print(sql)
dado = {
    'modelo': modelo,
    'montadora': montadora,
    'placa': placa,
    'id': id
}
cur.execute(sql, dado)

con.commit()
cur.close()
con.close()