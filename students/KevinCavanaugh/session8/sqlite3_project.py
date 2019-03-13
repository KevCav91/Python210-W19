import sqlite3
from sqlite3 import Error as sqlErr
import re as rex

from sqlite3 import Error as sql_err

#!/usr/bin/env python3

# ----------------------------------------------------------------------- #
# Title: sqlite3_project
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, started assignment, 03/05/2019
# ----------------------------------------------------------------------- #
def create_connection(db_file: str = 'C:\sqlite\databases\Python210FinalDB.db'):
    """ Create or connect to a SQLite database """
    try:
        con = sqlite3.connect(db_file)
    except sqlErr as se:
        raise Exception('SQL Error in create_connection(): ' + se.__str__())
    except Exception as e:
        raise Exception('General Error in create_connection(): ' + e.__str__())
    return con


# SQL Validators
def check_for_extra_semicolon(sql_str):
    """Checks for an extra semicolon"""
    # print(len("Select;Delete From T1; ID, Name FROM T1;".split(';')) > 2)
    try:
        if len(sql_str.split(';')) > 2:
            raise sqlErr("Extra Semi-Colon Detected!")
    except Exception as e:
        raise e


def check_for_or(sql_str):
    """Checks for an injected OR in tampered WHERE Clause"""
    # print(rex.search("WHERE", "SELECT * FROM T1 WHERE", rex.IGNORECASE))
    # print(rex.search("or","FROM T1 WHERE ID = 1 or 1 = 1".split('WHERE')[1], rex.IGNORECASE))
    try:
        if rex.search("WHERE", sql_str, rex.IGNORECASE):  # If it has a Where clause
            if rex.search(' or ', sql_str.split('WHERE')[1], rex.IGNORECASE) is not None:  # check injected OR
                raise sqlErr("OR Detected!")
    except Exception as e:
        raise e


def check_for_date(date_str):
    try:
        if rex.match("\d\d\d\d-\d\d-\d\d", str(date_str)) is None:  # Returns None if not matched
            raise sqlErr("Not a Date!")
    except Exception as e:
        raise e


def execute_sql_code(db_con: object = None, sql_code: str = ''):
    """ Execute SQL code on a open connection """
    try:
        if db_con is not None and sql_code != '':
            # Validate
            check_for_extra_semicolon(sql_code);
            check_for_or(sql_code);
            # Connect and Run
            with db_con:
                csr = db_con.cursor()
                csr.execute(sql_code)
        else:
            raise Exception('SQL Code or Connection is missing!')
    except sqlErr as se:
        raise Exception('SQL Error in execute_sql_code(): ' + se.__str__())
    except Exception as e:
        raise Exception('General Error in execute_sql_code(): ' + e.__str__())
    return csr


# Inventory
def ins_inventory(inventory_id: int, inventory_date: str):
    check_for_date(inventory_date)
    sql = str.format("INSERT INTO Inventories (InventoryID, InventoryDate) "
                     "VALUES ({id},'{date}');", id=inventory_id, date=inventory_date)
    return sql


def upd_inventory(inventory_id: int, inventory_date: str):
    check_for_date(inventory_date)
    sql = str.format("UPDATE Inventories SET InventoryDate = '{date}' "
                     "WHERE InventoryID = {id};", id=inventory_id, date=inventory_date)
    return sql


def del_inventory(inventory_id: int):
    sql = str.format("DELETE FROM Inventories WHERE InventoryID = {id};", id=inventory_id)
    return sql


def sel_inventory(inventory_id: int = None):
    if inventory_id is not None:
        inventory_id = ' WHERE inventory_id = ' + str(inventory_id)  # Will be validated at execution!
    else:
        inventory_id = ''
    sql = str.format("SELECT InventoryID, InventoryDate FROM Inventories{id};", id=inventory_id)
    return sql


if __name__ == '__main__':
    try:
        db = create_connection()
    except Exception as e:
        print('Connection failed!', e)

    # Test SQL creation
    sql_str = ins_inventory(inventory_id=3, inventory_date='2000-03-01')
    print(sql_str)
    sql_str = upd_inventory(inventory_id=3, inventory_date='2000-03-02')
    print(sql_str)
    sql_str = del_inventory(inventory_id=3)
    print(sql_str)
    sql_str = sel_inventory()
    print(sql_str)
    sql_str = sel_inventory(inventory_id=3)
    print(sql_str)

    # Test SQL validation
    try:
        check_for_or(sel_inventory(inventory_id="2 OR 1 = 1"))  # SQL Injection
    except Exception as e:
        print(e)
    try:
        check_for_extra_semicolon(sel_inventory(inventory_id="1;Delete From T1;"))  # SQL Injection
    except Exception as e:
        print(e)
    try:
        check_for_date(ins_inventory(inventory_id=3, inventory_date='03/03/2000'))  # Date Format Error
    except Exception as e:
        print(e)

    # Test SQL execution
    csr = execute_sql_code(db_con=db, sql_code=sel_inventory())
    for row in csr:
        print(row)
