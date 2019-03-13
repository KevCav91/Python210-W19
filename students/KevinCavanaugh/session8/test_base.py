
import base_class as dp

debugDP = False
debugIP = True

if __name__ == '__main__':
    # Test DataProcessor methods
    if debugDP == True:
        try: dp.DBProcessor.check_for_or("SELECT * FROM T1 WHERE ID = 1 or 1 = 1")
        except Exception as e: print(e)
        try: dp.DBProcessor.check_for_extra_semicolon("SELECT * ;Delete From T1; FROM T1;")
        except Exception as e: print(e)
        try: dp.DBProcessor.check_for_date('01/01/2000')
        except Exception as e: print(e)

        dbp = dp.DBProcessor(':memory:')
        print(dbp.build_ins_code())
        print(dbp.build_upd_code())
        print(dbp.build_del_code())
        print(dbp.build_sel_code())
        print(dbp.build_sel_code())
        csr = dbp.execute_sql_code("Select 5 + 5;")
        for e in csr:
            print(e)
        print(dbp.execute_sql_code("Select 5 + 5;"))
        dbp.db_con.close()

    if debugIP == True:
        ip = dp.InventoryProcessor(':memory:')
        print(ip.build_ins_code(inventory_id=1, inventory_date='2000-01-01'))
        print(ip.build_upd_code(inventory_id=1, inventory_date='2000-02-02'))
        print(ip.build_del_code(inventory_id=1))
        print(ip.build_sel_code())

        # Create a table for testing
        crs = ip.db_con.cursor()
        crs.execute("CREATE TABLE Inventories (InventoryID int, InventoryDate date);")
        ip.db_con.commit()
        for row in crs.execute("Select name, sql From sqlite_master Where type='table;'"):
            print(row)
        ip.db_con.commit()

        # Test SQL Transactions
        ip.execute_sql_code(ip.build_ins_code(inventory_id=1, inventory_date='2000-01-01')).close()
        for row in ip.execute_sql_code(ip.build_sel_code()):
            print(row)

    ip.execute_sql_code(ip.build_upd_code(inventory_id=1, inventory_date='2000-02-02')).close()
    for row in ip.execute_sql_code(ip.build_sel_code(inventory_id=1)):
        print(row)

    ip.execute_sql_code(ip.build_del_code(inventory_id=1)).close()
    for row in ip.execute_sql_code(ip.build_sel_code()):
        print(row)

