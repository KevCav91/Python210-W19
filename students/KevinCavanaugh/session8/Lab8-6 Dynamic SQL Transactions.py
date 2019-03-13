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
            csr = db_con.cursor()
            csr.execute(sql_code)
            db_con.commit()
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
            sql_str = 'CREATE TABLE ' + name_of_table + '('
            for col in col_names:
                sql_str += str(col) + ' [text], '
            sql_str = sql_str[0:-2] + ');'  # Strip off the last comma
    except Exception as e:
        raise Exception('Error in create_table(): ' + e.__str__())
    return sql_str

def create_select_code(name_of_table, col_names=[None]):
    """ create table select code """
    sql_str = ''
    try:
        if col_names is None:
            raise Exception('You must provide at least one column name!')
        else:
            sql_str = 'SELECT \n'
            for col in col_names:
                sql_str += str(col) + ', '
            sql_str = sql_str[0:-2] + '\n' # Strip off the last comma
            sql_str += 'FROM ' + name_of_table + ';'
    except Exception as e:
        raise Exception('Error in create_select_code(): ' + e.__str__())
    return sql_str

def create_insert_code(name_of_table, col_names=[None], col_values=[None],):
    """ create table insert code """
    sql_str = ''
    try:
        if col_names is None:
            raise Exception('You must provide at least one column name!')
        else:
            sql_str = 'INSERT INTO ' + str(name_of_table).strip() + '\n('
            for col in col_names:
                sql_str += str(col) + ', '
            sql_str = sql_str[0:-2] + ')'  # Strip off the last comma
        if col_values is None:
            raise Exception('You must provide at least one column value!')
        else:
            sql_str += '\nVALUES\n('
            for col in col_values:
                sql_str += str(col) + ', '
            sql_str = sql_str[0:-2] + ');'  # Strip off the last comma
    except Exception as e:
        raise Exception('Error in create_insert_code(): ' + e.__str__())
    return sql_str

def create_update_code(name_of_table, col_names=[None], col_values=[None], where_col = None, where_equals_value = None):
    """ create table update code """
    sql_str = ''
    try:
        if col_names is None:
            raise Exception('You must provide at least one column name!')
        elif col_values is None:
            raise Exception('You must provide at least one column value!')
        elif len(col_names) != len(col_values):
            raise Exception('You must provide one value for each column')
        elif where_col is None or where_equals_value is None:
            raise Exception('You must provide a where column and an equals value')
        else:
            sql_str = 'UPDATE ' + str(name_of_table).strip() + '\nSET\n\t'
            counter = 0
            while counter < len(col_names):
                sql_str += str(col_names[counter]).strip() \
                            + ' = ' + str(col_values[counter]).strip() + ', \n\t'
                counter += 1
            sql_str = (sql_str.strip())[0:-1] + ''  # Strip off the last comma
            sql_str += '\nWHERE ' + where_col + " = " + where_equals_value
    except Exception as e:
        raise Exception('Error in create_update_code(): ' + e.__str__())
    return sql_str

def create_delete_code(name_of_table, where_col = None, where_equals_value = None):
    """ create table delete code """
    sql_str = ''
    try:
        if where_col is None or where_equals_value is None:
            raise Exception('You must provide a where column and an equals value')
        else:
            sql_str = 'DELETE FROM ' + str(name_of_table).strip()
            sql_str += '\nWHERE ' + where_col + " = " + str(where_equals_value).strip()
    except Exception as e:
        raise Exception('Error in create_delete_code(): ' + e.__str__())
    return sql_str


def main_menu():
    print('\n', '='*50, sep='')
    print("Choose an option by number: ")
    print("\t 1 =  Create or Connect to a new file database")
    print("\t 2 =  Create a new memory database")
    print("\t 3 =  Create a new table")
    print("\t [s] =  Select from table")
    print("\t [i] =  Insert into table")
    print("\t [u] =  Update in table")
    print("\t [d] =  Delete from table")
    print('Type exit to quit program!')
    print('='*50, '\n', sep='')


if __name__ == '__main__':
    dbconnection = None
    while True:
        try:
            main_menu()
            choice = input("Option: ").strip()
            if choice == '1':
                fn = input("Enter file name and path: ").strip()
                dbconnection = create_connection(fn)
            elif choice == '2':
                dbconnection = create_connection(':memory:')
            elif choice == '3':
                t = input("Enter a name for the table: ").strip()
                cols = input("Enter a comma separated list of column names (col1,col2,etc...): ").strip()
                sql = create_table_code(t, cols.split(','))
                opt = input('\nPreview:\n\n\t' + sql + '\n\nCreate the following table?(y/n):')
                if opt.lower() == 'y':
                    execute_sql_code(db_con=dbconnection, sql_code=sql).close() # Close Cursor
                else:
                    print('Info ->\tTable creation cancelled!')
            elif choice == 's':
                t = input("Enter a name for the table: ").strip()
                cols = input("Enter a comma separated list of column names (col1,col2,etc...): ").strip()
                sql = create_select_code(t, cols.split(','))
                print('\nCode Used : ' + sql + '\n')
                csrData = execute_sql_code(db_con=dbconnection, sql_code=sql)  # Don't close cursor
                for row in csrData:
                    for col in row:
                        print(col, end=' | ')
                    print()
                csrData.close()  # Now close cursor!
            elif choice == 'i':
                t = input("Enter a name for the table: ").strip()
                cols = input("Enter a comma separated list of column names (col1,col2,etc...): ").strip()
                colvals = input("Enter a comma separated list of column VALUES (col1,col2,etc...): ").strip()
                sql = create_insert_code(t, cols.split(','), colvals.split(','))
                opt = input('\nPreview:\n\n' + sql + '\n\nInsert this data?(y/n):')
                if opt.lower() == 'y':
                    execute_sql_code(db_con=dbconnection, sql_code=sql).close() # Close Cursor
            elif choice == 'u':
                t = input("Enter a name for the table: ").strip()
                cols = input("Enter a comma separated list of column names (col1,col2,etc...): ").strip()
                colvals = input("Enter a comma separated list of column VALUES (col1,col2,etc...): ").strip()
                wc = input("Enter one WHERE column Name: ").strip()
                wv = input("Enter one WHERE column Equals Value: ").strip()
                sql = create_update_code(t, cols.split(','), colvals.split(','),where_col=wc, where_equals_value=wv)
                opt = input('\nPreview:\n\n' + sql + '\n\nUpdate this data?(y/n):')
                if opt.lower() == 'y':
                    execute_sql_code(db_con=dbconnection, sql_code=sql).close() # Close Cursor
            elif choice == 'd':
                t = input("Enter a name for the table: ").strip()
                wc = input("Enter one WHERE column Name: ").strip()
                wv = input("Enter one WHERE column Equals Value: ").strip()
                sql = create_delete_code(t, where_col=wc, where_equals_value=wv)
                opt = input('\nPreview:\n\n' + sql + '\n\nDelete this data?(y/n):')
                if opt.lower() == 'y':
                    execute_sql_code(db_con=dbconnection, sql_code=sql).close() # Close Cursor
            elif choice.lower() == 'exit':
                break
            else:
                print('Please enter a number for the option you want!')
        except Exception as e:
            print('Error ->\t', e.__str__())
    dbconnection()

