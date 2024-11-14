class computer:
    def __init__(self):
        self.__max_price= 900
    def sell(self):
        print(self.__max_price)
    def setmaxprice(self, price):
        self.__max_price= price
a= computer()
a.sell()
a.__max_price= 1000
a.sell()
a.setmaxprice(1200)
a.sell()