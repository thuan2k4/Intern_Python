from abc import ABC, abstractmethod
class Human:
    #Constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #Method
    def Show_Information(self):
        print(f"Name is {self.name}, Age is {self.age}, Gender is {self.gender}")

    #Override method
    def Salary(self):
        pass


#Create object
Human1 = Human("John", 20, "Male")
Human1.Show_Information()

class arithmetic:
    def __init__(self, numeric):
        self.numeric = numeric

    #Magic Method
    def __add__(self, other):
        return self.numeric + other.numeric
    
    def __str__(self):
        return f"The value of numeric is {self.numeric}"
    
    def __mul__(self, other):
        return self.numeric * other.numeric
    
    def __eq__(self, other):
        return self.numeric == other.numeric
    
    def __ne__(self, other):
        return self.numeric != other.numeric
    
    def __gt__(self, other):
        return self.numeric > other.numeric
    
    def __ge__(self, other):
        return self.numeric >= other.numeric
    
    def __lt__(self, other):
        return self.numeric < other.numeric
    
    def __le__(self, other):
        return self.numeric <= other.numeric

a = arithmetic(10)
b = arithmetic(20)
print(f"{a}, {b}")
print(a + b)
print(a * b)
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

class ITer(Human): #Inheritance
    def __init__(self, name, age, gender, ID_Card):
        super().__init__(name, age, gender)
        self.__ID_Card = ID_Card #Private Attribute
    
    def Salary(self):
        return 100000
    
class BA(Human): #Inheritance
    def __init__(self, name, age, gender, ID_Card):
        super().__init__(name, age, gender)
        self.__ID_Card = ID_Card #Private Attribute
    
    def Salary(self):
        return 200000
    
it1 = ITer("John", 20, "Male", "1234567890")
it1.Show_Information()
try:
    print(it1.__ID_Card)
except AttributeError:
    print("Error: Private attribute")
print(it1.Salary())

ba1 = BA("Jane", 25, "Female", "1234567890")
print(ba1.Salary())

#Abstract (Interface) Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle1 = Circle(10)
print(circle1.area())
