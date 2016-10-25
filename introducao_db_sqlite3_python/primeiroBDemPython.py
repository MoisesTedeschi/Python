#!/usr/bin/python3
#Introdução a banco de dados com python3

import sqlite3

def main():
    db = sqlite3.connect("son.bd")
    db.row_factory = sqlite3.Row #Traz o objeto da linha correspondente, mas precisa ser visualizado como dicionário.
    db.execute("drop table if exists teste")
    db.execute("create table teste(id int, nome text)")
    db.execute("insert into teste(id, nome) values(?, ?)", (1, "Bia"))
    db.execute("insert into teste(id, nome) values(?, ?)", (2, "Fernanda"))
    db.execute("insert into teste(id, nome) values(?, ?)", (3, "Nath"))
    db.execute("insert into teste(id, nome) values(?, ?)", (4, "Paula"))

    db.commit()

    cursor = db.execute("select id, nome from teste order by nome")

    for row in cursor:
        print(dict(row)) #Visualização em forma de dicionário por causa do row_factory

if __name__ == "__main__" : main()
