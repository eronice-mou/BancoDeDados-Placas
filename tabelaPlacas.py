import mysql.connector

try:
    #Criar conexão ao banco de dados
    con = mysql.connector.connect(host='localhost', database='placaadata', user='root', password='')

#Declaração sql a ser executada
    criar_tabela_sql = """ CREATE TABLE tbl_placas(
        IdProduto int(11) not null,
        Ordemdeproducao int not null,
        Sequencia int not null,
        Horariodaoperacaodaplaca date,
        PRIMARY KEY (IdProduto)
    )"""

#Criar cursor e executar SQL no banco de dados
    cursor = con.cursor()
    cursor.execute(criar_tabela_sql)
    print("Tabela criada com sucesso!")
except mysql.connector.Error as erro:
    print("Falha ao criar tabela no mysql: {}".format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySql finalizada.")