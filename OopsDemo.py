# Self: is a reference to the current instance of the class. It is used to access variables that belong to the class.
# example: self.a, self.b, self.num

# Instance variables will be initialized in the constructor and can be accessed using self.
# Instance variables are defined in the constructor and are unique to each instance of the class.

class Calculator:
    num=100 # Class variables


    # default Constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("auto triggered")

    def getdata(self):
        print("class method")
        
    def summation(self):
        return self.a + self.b + self.num
    
    
obj1 = Calculator(2,3)
obj1.getdata()
print(obj1.summation())

obj = Calculator(4,5)
obj.getdata()
print(obj.summation())

