class abc:
    __pria = 27
    def __primet(self):
        print("I am inside a private method")
    def hello(self):
        print(abc.__pria)
a= abc()
a.hello()
a.__pria