import sqlite3
from sqlite3 import Error as SqlErr

try:
    # Create or Connect to a DB
    db_con = sqlite3.connect(':memory:')
    with db_con:
        csr = db_con.cursor()
        csr.execute("create table Demo (ID [integer], Name [text]);")  # SQL requires a semi-colon!
        # Insert some data
        csr.execute("insert into Demo (ID, Name) values (?, ?);", (1, 'A'))  # requires a Tuple
        csr.execute("insert into Demo (ID, Name) values (?, ?);", (2, 'B'))  # requires a Tuple
        # Select some data
        csr.execute("select ID, Name from Demo;")
        rows = csr.fetchall()  # for multiple rows
        for row in rows:
            print(row, type(row))
        csr.execute("select ID, Name from Demo where ID = ?;", (1, ))  # remember the extra comma!
        row = csr.fetchone()  # for only one row!
        print(row, type(row))
        csr.close()  # Always close the cursor when your done
    # db_con.close() # Not, needed since the "with" automatically closes the connection
except SqlErr as se:
    print(se)
except Exception as e:
    print(e)
