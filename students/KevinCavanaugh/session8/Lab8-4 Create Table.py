import sqlite3
from sqlite3 import Error as sqlErr

def create_connection(db_file):
    """ Create or connect to a SQLite database """
    try:
        con = sqlite3.connect(db_file)
        print('SQLite Version is: ', sqlite3.version)
    except sqlErr as se:
        raise Exception('SQL Error in create_connection(): ' + se.__str__())
    except Exception as e:
        raise Exception('General Error in create_connection(): ' + e.__str__())
    return con

def execute_sql_code(db_con = None, sql_code=''):
    """ Execute SQL code on a open connection """
    try:
        if db_con is not None and sql_code != '':
            with db_con:
                csr = db_con.cursor()
                csr.execute(sql_code)
        else:
            raise Exception('SQL Code or Connection is missing!')
    except sqlErr as se:
        raise Exception('SQL Error in create_connection(): ' + se.__str__())
    except Exception as e:
        raise Exception('General Error in create_connection(): ' + e.__str__())
    return csr

def create_table_code(name_of_table, col_names=[None]):
    """ Create table code """
    sql_str = ''
    try:
        if col_names is None:
            raise Exception('You must provide at least one column!')
        else:
            sql_str = 'create table ' + name_of_table + ' ('
            for col in col_names:
                sql_str += str(col) + ' [text], '
            sql_str = sql_str[0:-2] + ');'  # Strip off the last comma
    except Exception as e:
        raise Exception('Error in create_table_code(): ' + e.__str__())
    return sql_str


def main_menu():
    print('\n', '='*50, sep='')
    print("Choose an option by number: ")
    print("\t 1 =  Create or Connect to a new file database")
    print("\t 2 =  Create a new memory database")
    print("\t 3 =  Create a new table")
    print('Type exit to quit program!')
    print('='*50, '\n', sep='')

if __name__ == '__main__':
    dbconnection = None
    while True:
        try:
            main_menu()
            choice = input("Option: ")
            if choice == '1':
                fn = input("Enter file name and path: ")
                dbconnection = create_connection(fn)
            elif choice == '2':
                dbconnection = create_connection(':memory:')
            elif choice == '3':
                name = input("Enter a name for the table: ")
                cols = input("Enter a comma separated list of column names (col1,col2,etc...): ").strip()
                sql = create_table_code(name, cols.split(','))
                opt = input('\nPreview:\n\n' + sql + '\n\nCreate the following table?(y/n):')
                if opt.lower() == 'y':
                   csr = execute_sql_code(db_con=dbconnection, sql_code=sql)
                   csr.close()
                else:
                    print('Info ->\tTable creation cancelled!')
            elif choice.lower() == 'exit':
                break
            else:
                print('Please enter a number for the option you want!')
        except Exception as e:
            print('Error ->\t', e.__str__())

    dbconnection.close()
