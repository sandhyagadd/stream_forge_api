##class TestClass:
##    def __init__(self,a):
##        self.a = a
##
##    def __call__(self,b):
##        return self.a * b
##
##obj = TestClass(5)
##print(obj(8))



##class myclass:
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age
##
##    def __repr__(self):
##        return f"{self.name, self.age}"
##        
##
####    def __str__(self):
####        return f"{self.name, self.age}"
##
##
##obj = myclass("saurabh", 35)
##print(repr(obj))
##print(str(obj))
##


class Customer:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "Customer('{}')".format(self.name)
    def __str__(self):
        return f"cunstomer name is {self.name}"

cus_1 = Customer("Thusi")
print(repr(cus_1)) #print(cus_1.__repr__()) 
print(str(cus_1)) #print(cus_1.__str__())




def fun(n):
    return lambda a: a*n

duble = fun(2)
print(duble(2))










