import sqlite3
from sqlite3 import Error as SqlErr

try:
    # Create or Connect to a DB
    db_con = sqlite3.connect('SimpleDemo.db')
    # Create a table in the DB
    csr = db_con.cursor()
    csr.execute("create table Demo (ID [integer], Name [text]);") # SQL requires a semi-colon!
    # Insert some data
    csr.execute("insert into Demo (ID, Name) values (1, 'A'), (2, 'B');")  # SQL uses only Single quotes for strings!
    # Select some data
    csr.execute("select ID, Name from Demo;") # SQL can use the * symbol to indicate all columns!
    rows = csr.fetchall()
    csr.close()  # Always close the cursor when your done
    db_con.close()  # Always close the connection when your done
    for row in rows:
        print(row, type(row))
except SqlErr as se:
    print(se)
except Exception as e:
    print(e)


