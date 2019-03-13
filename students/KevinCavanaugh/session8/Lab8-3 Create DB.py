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


def main_menu():
    """ Present a menu to the user """
    print('\n', '='*50, sep='')
    print("Choose an option by number: ")
    print("\t 1 =  Create or Connect to a new file database")
    print("\t 2 =  Create a new memory database")
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
            elif choice.lower() == 'exit':
                break
            else:
                print('Please enter a number for the option you want!')
        except Exception as e:
            print('Error ->\t', e.__str__())