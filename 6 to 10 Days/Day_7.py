################################## Day 7: 69 Days of Python #####################################

# Python Classes/Objects
# Create a Class and Object
class MyClass:
    x = 5

myobj = MyClass()
print(myobj.x)

# The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# The __str__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Keyur", 20)
print(p1)

# Object Methods
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Employee("Keyur", 20)
p1.myfunc()

# The self Parameter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("Keyur", 20)
p1.myfunc()

# Modify Object Properties
p1.age = 40

# Delete Object Properties
# del p1.age

# Delete Objects
# del p1

# The pass Statement
class MyClass:
    pass


# Python Inheritance
# Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Keyur", "Bhatiya")
x.printname()

# Child Class
class Student(Person):
    pass

# Add the __init__() Function
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Keyur", "Bhatiya")
x.printname()

# Add Properties and Methods
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

x = Student("Keyur", "Bhatiya", 2004)
x.welcome()


# Python Iterators
# Simple Iteration
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
for x in iter(("orange", "mango", "pineapple", "grapes")):
    print(x)

# Create an Iterator
class MyIterator:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyIterator()
for x in iter(myclass):
    print(x)


# Python Polymorphism
# Function Polymorphism
print("Hello, Keyur")
print(len({"brand": "Ford", "model": "Mustang", "year": 1964}))

# Class Polymorphism
class Animal:
    def makeSound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def makeSound(self):
        print("The dog barks")

Animal().makeSound()
Dog().makeSound()

# Inheritance Class Polymorphism
class Car:
    def move(self):
        print("The car moves")

class BMW(Car):
    def move(self):
        print("The BMW moves")

Car().move()
BMW().move()


# Python Scope
# Global and Local Scope
x = "awesome"

def greet():
    x = "fantastic"
    print("Python is " + x)

greet()
print("Python is " + x)

# Function Inside Function
def outer():
    x = "awesome"
    def inner():
        nonlocal x
        x = "fantastic"
    inner()
    print("My tutorial is " + x)

outer()

# Global Keyword
x = 300

def myfunc():
    global x
    x = 80000

myfunc()
print(x)

# Nonlocal Keyword
def myfunc():
    x = 300
    def myinnerfunc():
        nonlocal x
        x = 200
    myinnerfunc()
    print(x)

myfunc()
