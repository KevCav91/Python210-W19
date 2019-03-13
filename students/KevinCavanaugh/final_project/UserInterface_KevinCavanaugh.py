import DataProcessor_KevinCavanaugh as dp
from DataProcessor_KevinCavanaugh import InventoryProcessor as ip
from DataProcessor_KevinCavanaugh import InventoryCountsProcessor as icp
from DataProcessor_KevinCavanaugh import ProductProcessor as pp
import DataModel_KevinCavanaugh as dm

# Fill Products
# Fill Inventory Counts

debugDP = False

if __name__ == '__main__':

    pp = dp.ProductProcessor(':memory:')
    # Create a table for testing
    crs = pp.db_con.cursor()
    crs.execute("CREATE TABLE Products (ProductID int Primary Key, ProductName varchar(100));")
    pp.db_con.commit()
    pp.execute_sql_code(pp.build_ins_code(product_id=100, product_name='Mouse'))
    pp.db_con.commit()
    pp.execute_sql_code(pp.build_ins_code(product_id=200, product_name='Keyboard'))
    pp.db_con.commit()

    print(pp.build_sel_code())
    plst = []
    for row in crs.execute(pp.build_sel_code()):
        print(row)
        plst.append(dm.Product(row[0], row[1]))
    print(plst)
    pp.db_con.commit()
    pp.db_con.close()
