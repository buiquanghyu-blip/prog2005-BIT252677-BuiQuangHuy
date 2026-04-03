class Book:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

book1 = Book("Python", 30000)

print("Giá sách:", book1.get_price())
