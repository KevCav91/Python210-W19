import sqlite3
from sqlite3 import Error as sqlErr


def create_connection(db_file):
    try:
        con = sqlite3.connect(db_file)
        print('SQLite Version is: ', sqlite3.version)
    except sqlErr as se:
        raise Exception('SQL Error in create_connection(): ' + se.__str__())
    except Exception as e:
        raise Exception('General Error in create_connection(): ' + e.__str__())
    return con


def execute_sql_code(db_con = None, sql_code=''):
    try:
        if db_con is not None and sql_code != '':
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
    """ create table code """
    sql_str = ''
    try:
        if col_names is None:
            raise Exception('You must provide at least one column!')
        else:
            sql_str = 'CREATE TABLE ' + name_of_table + '\n('
            for col in col_names:
                sql_str += str(col) + ' [text], '
            sql_str = sql_str[0:-2] + ');'  # Strip off the last comma
    except Exception as e:
        raise Exception('Error in create_staging_table(): ' + e.__str__())
    return sql_str


def create_insert_code(name_of_table, col_names=[None], col_values=[None],):
    """ create staging table insert code """
    sql_str = ''
    try:
        if col_names is None:
            raise Exception('You must provide at least one column name!')
        else:
            sql_str = 'INSERT INTO ' + name_of_table + '\n('
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
    """ create staging table update code """
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
            sql_str = 'UPDATE ' + name_of_table + '\nSET\n\t'
            counter = 0
            while counter < len(col_names):
                sql_str += str(col_names[counter]) + ' = ' + str(col_values[counter]) + ', \n\t'
                counter += 1
            sql_str = (sql_str.strip())[0:-1] + ''  # Strip off the last comma
            sql_str += '\nWHERE ' + where_col + " = " + where_equals_value
    except Exception as e:
        raise Exception('Error in create_update_code(): ' + e.__str__())
    return sql_str


def create_delete_code(name_of_table, where_col = None, where_equals_value = None):
    """ create staging table delete code """
    sql_str = ''
    try:
        if where_col is None or where_equals_value is None:
            raise Exception('You must provide a where column and an equals value')
        else:
            sql_str = 'DELETE FROM ' + name_of_table
            sql_str += '\nWHERE ' + where_col + " = " + where_equals_value
    except Exception as e:
        raise Exception('Error in create_delete_code(): ' + e.__str__())
    return sql_str


def create_select_code(name_of_table, col_names=[None]):
    """ create staging table select code """
    sql_str = ''
    try:
        if col_names is None:
            raise Exception('You must provide at least one column name!')
        else:
            sql_str = 'SELECT \n\t'
            for col in col_names:
                sql_str += str(col) + ', \n\t'
            sql_str = sql_str[0:-2] + '\n' # Strip off the last comma
            sql_str += 'FROM ' + name_of_table + ';'
    except Exception as e:
        raise Exception('Error in create_select_code(): ' + e.__str__())
    return sql_str

# SQL Validators
def check_for_extra_semicolon(SQLStr):
    try:
        if SQLStr.find(';') != -1:
            raise Exception("Extra Semi-Colon Detected!")
    except Exception as e:
        raise e


def check_for_or(SQLStr):
    try:
        if SQLStr.find('or') != -1:
            raise Exception("OR Detected!")
    except Exception as e:
        raise e


if __name__ == '__main__':

    try:
        print('\ntest CREATE TABLE','-'*40, '\n')
        print(create_table_code('StagingStudents', ['ID','Name','Email']))
    except Exception as e:
        print(e)

    try:
        print('\ntest SELECT','-'*40, '\n')
        print(create_select_code('StagingStudents', ['ID','Name','Email']))
    except Exception as e:
        print(e)

    try:
        print('\ntest INSERT','-'*40, '\n')
        print(create_insert_code('StagingStudents', ['ID','Name','Email'], [1,'Bob Smith', 'BSmith@gomail.com']))
    except Exception as e:
        print(e)

    try:
        print('\ntest UPDATE','-'*40, '\n')
        print(create_update_code('StagingStudents', ['Name','Email'], ['Rob Smith', 'RSmith@gomail.com'], 'ID', '1'))
    except Exception as e:
        print(e)

    try:
        print('\ntest DELETE','-'*40, '\n')
        print(create_delete_code('StagingStudents', 'ID', '1'))
    except Exception as e:
        print(e)