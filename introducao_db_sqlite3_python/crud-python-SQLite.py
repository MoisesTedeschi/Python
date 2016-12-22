#!/usr/bin/python3
#Criação de um CRUD em python3 com SQLite3
#Autor: Moisés Tedeschi

import sqlite3
#Funções do CRUD
#Create - inserinto os dados na tabela.
def insert(db, row):
    db.execute("insert into tb_pessoas(id, nome) values(?, ?)", (row["id"], row["nome"]))
    db.commit()

#Retrieve - Selecionando um id na tabela. 
def retrieve(db, id):
    ponteiro = db.execute("select * from tb_pessoas where id = ?", (id,))
    return ponteiro

#Update - Alterando valor já existente na tabela.
def update(db, row):
    db.execute("update tb_pessoas set nome = ? where id = ?", (row["nome"], row["id"]))
    db.commit

#Delete - Deletando um valor já existente nos registros da tabela.
def delete(db, id):
    db.execute("delete from tb_pessoas where id = ?", (id,))
    db.commit

#Criei uma função de display só para exibir todos os registros cadastrados no banco de dados.
def display(db):
    exibir = db.execute("select * from tb_pessoas order by id")
    for row in exibir:
        print(" {}: {}".format(row["id"], row["nome"]))
    

def main():
    db = sqlite3.connect("pessoas.bd")
    db.row_factory = sqlite3.Row #Traz o objeto da linha correspondente, mas precisa ser visualizado como dicionário.
    db.execute("drop table if exists tb_pessoas")
    db.execute("create table tb_pessoas(id int, nome text)")
    print("Criando uma tabela no banco!\n")

    insert(db, dict(id=1, nome="Marta"))
    insert(db, dict(id=2, nome="Fernanda"))
    insert(db, dict(id=3, nome="Paulo"))
    insert(db, dict(id=4, nome="João"))
    insert(db, dict(id=5, nome="Algusto"))

    display(db) #Exibindo todos os registro do banco.
    print("\nRetrieve\n") #Recuperando 2 registros do banco.
    print(dict(retrieve(db, 1)), dict(retrieve(db, 2)))

    print("\nUpdate\n")
    update(db, dict(id = "5", nome="Pedro Algusto"))
    display(db)

    print("\nDelete\n")
    delete(db, 1)
    display(db)
   
if __name__ == "__main__" : main()
