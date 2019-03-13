from datetime import datetime


class Product(object):

    def __init__(self, product_id: int, product_name: str):
        self.product_id = product_id
        self.product_name = product_name

    def __str__(self):
        return f'{self.product_id},{self.product_name}'

    def __repr__(self):
        return f'{Product},[{str(self.__dict__())}'

    def __dict__(self):
        return {"product_id": self.product_id, "product_name": self.product_name}

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        if type(product_id) is not int:
            raise TypeError("Requires integer!")
        if product_id <= 0:
            raise ValueError("Requires value greater than zero!")
        else:
            self.__product_id = product_id

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = str(product_name).strip()

    # Add properties and validation
    # product_id > 0


class InventoryCount(object):

    def __init__(self, product: Product, count: int):
        self.product = product
        self.count = count

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        if type(count) is not int: raise TypeError("Requires integer!")
        if count <= 0:
            raise ValueError("Requires value greater than zero!")
        else:
            self.__count = count

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        if type(product) is not Product:
            raise TypeError("Requires product object!")
        else:
            self.__product = product

    # Add properties and validation
    # count >= 0
    # product is Product


class Inventory(object):
    def __init__(self, inventory_id: int, inventory_date: datetime.date, inventory_counts: InventoryCount = [None]):
        self.inventory_id = inventory_id
        self.inventory_date = inventory_date
        if inventory_counts is not None:
            self.inventory_counts = inventory_counts

    @property
    def inventory_id(self):
        return self.__inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        if inventory_id <= 0:
            raise ValueError("Requires value greater than zero!")
        else:
            self.__inventory_id = inventory_id

    @property
    def inventory_date(self):
        return self.__inventory_date

    @inventory_date.setter
    def inventory_date(self, inventory_date):
        # if type(inventory_date) is not datetime:
        #     raise TypeError("Requires datetime object!")
        # else:
        self.__inventory_date = inventory_date

    @property
    def inventory_counts(self):
        return self.__inventory_counts

    @inventory_counts.setter
    def inventory_counts(self, inventory_counts):
        # if type(inventory_counts) is not InventoryCount:
        #     raise TypeError("Requires InventoryCount Object")
        # else:
        self.__inventory_counts = inventory_counts


    # Add properties and validation
    # inventory_id > 0
    # date is datetime
    # inventory_count is inventory_count


if __name__ == '__main__':
    p1 = Product(100, "ProdA")
    p2 = Product(200, "ProdB")
    ic1 = InventoryCount(p1, 15)
    ic2 = InventoryCount(p2, 45)
    invJan0119 = Inventory(1, '2020-01-01', [ic1,ic2])
    for ic in invJan0119.inventory_counts:
        print('Jan 2019 -', ic.product.product_name, ' = ', ic.count)
    print(p1, str(p1), p1.__str__())
    print(repr(p1))
    print(p1.__dict__())