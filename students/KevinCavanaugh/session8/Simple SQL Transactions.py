import sqlite3
from sqlite3 import Error as SqlErr

def create_demo(con):
    with db_con:
        csr = db_con.cursor()
        csr.execute("CREATE TABLE IF NOT EXISTS Demo (ID [integer], Name [text]);")
        db_con.commit()

def sel_demo(con):
    with db_con:
        csr = db_con.cursor()
        csr.execute("SELECT * FROM DEMO;")
        db_con.commit()
        return csr

def ins_demo(con, values=[None]):
    if values is not None:
        with db_con:
            csr = db_con.cursor()
            csr.execute("INSERT INTO Demo (ID, Name) values (?,?);", values)
            db_con.commit()

def upd_demo(con, values=[None]):
    if values is not None:
        with db_con:
            csr = db_con.cursor()
            csr.execute("UPDATE Demo SET ID = ?, Name = ? WHERE ID = ?;", values)
            db_con.commit()

def del_demo(con, values=[None]):
    if values is not None:
        with db_con:
            csr = db_con.cursor()
            csr.execute("DELETE FROM Demo WHERE ID = ?;", values)
            db_con.commit()

if __name__ == '__main__':
    db_con = sqlite3.connect('Lab8-5.db')
    create_demo(db_con)

    ins_demo(db_con, [1,'Bob'])  # Must use single quotes
    for row in sel_demo(db_con): print(row)

    upd_demo(db_con,[1,'Rob', 1])
    for row in sel_demo(db_con): print(row)

    del_demo(db_con, [1])
    for row in sel_demo(db_con): print(row)


