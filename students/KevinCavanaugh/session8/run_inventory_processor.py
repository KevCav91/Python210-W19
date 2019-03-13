import base_class as dp

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
