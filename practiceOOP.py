
# Question 01

# class programmer:
#     company="Microsoft"
#     def __init__(self,name,salary,pincode):
#         self.name=name
#         self.salary=salary
#         self.pincode=pincode

# p=programmer("Ansir",120000,1543)
# print(p.name,p.salary,p.pincode)        



# Question 02

# class calculator:
#     def __init__(self,n):
#         self.n=n
        
#     def square(self):
#         print(f"the square is :{self.n*self.n}")
        
#     def cube(self):
#         print(f"the cube is :{self.n*self.n*self.n}")
        
#     def square_Root(self):
#         print(f"the square_root is :{self.n**1/2}")    
# a=calculator(4)
# a.square()
# a.cube()
# a.square_Root()        


# Question 03
# NO


# Question 04
# class calculator:
#     def __init__(self,n):
#         self.n=n
        
#     def square(self):
#         print(f"the square is :{self.n*self.n}")
        
#     def cube(self):
#         print(f"the cube is :{self.n*self.n*self.n}")
        
#     def square_Root(self):
#         print(f"the square_root is :{self.n**1/2}") 
        
#     @staticmethod
#     def greet():
#         print("Hello Ansir")   
# a=calculator(4)
# a.greet()
# a.square()
# a.cube()
# a.square_Root() 


# Question 05

# import random

# class Train:
#     def __init__(self, TrainNo):
#         self.trainNo = TrainNo

#     def book(self, fro, to):
#         print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")

#     def getStatus(self):
#         print(f"The train number {self.trainNo} runs on time")

#     def getfare(self, fro, to):
#         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {random.randint(222, 5555)}")

# t = Train(1234)
# t.book("Lahore", "Karachi")
# t.getStatus()
# t.getfare("Okara", "Depalpur")


# question 06
# No effect


#  chapter 11



# multiple inheritence
# class Employee:
#     company = "ITC"
#     name = "Ali"
#     salary = 120000
    
#     def show(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# class Coder:
#     language = "Python"
    
#     def show_language(self):
#         print(f"The coder uses the language: {self.language}")
        
# class Programmer():
#     company = "ITC Infotech"  
    
#     def show_language_details(self):
#         print(f"The name is {self.company} and he is good with {self.language}")

# # Creating an instance of the Programmer class
# a = Programmer()
# a.show()  # From Employee class
# a.show_language()  # From Coder class
# a.show_language_details()  # From Programmer class





# multi level in heritance
# class Employee:
#     a=1
    
    
# class Programmer(Employee):
#     b=2
    
    
# class Manager(Programmer):
#     c=3
    
    
# o=Employee()
# print(o.a)

# o=Manager()
# print(o.a,o.b,o.c)


# super keyword
# class Employee:
    
#     def __init__(self):
#         print(" Employee constructor")
#     a=1
    
    
# class Programmer(Employee):
#     def __init__(self):
#         print(" programmer constructor")
#     b=2
    
    
# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()
#         print(" Manager constructor")
#     c=3
    
# o=Manager()
# print(o.a,o.b,o.c)



# class method , property and setter

# class Employee:
#     a = 1  # Class attribute
    
#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")
    
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name(self, value):
#         self.fname=value.split(" ")[0]
#         self.lname=value.split(" ")[1]

# e = Employee()
# Employee.a = 45  

# # Set the name using the setter
# e.name = "Ansir Ali"

# print(e.fname, e.lname)

# e.show()


# operator overloading
# class Number:
#     def __init__(self,n):
#         self.n=n
#     def __add__(self,num): # ya theek jha
#         return self.n + num.n  
        
# n=Number(1)
# m=Number(2)
# print(n+m) # ya method wrong ha python operators ko b as a class ly ly ga





# practice set 11

# Q 01
# class twoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

#     def show(self):
#         print(f" the vector is {self.i}i+ {self.j}j") 

# class threeDvector(twoDVector):
    
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k

#     def show(self):
#         print(f" the vector is {self.i}i+ {self.j}j + {self.k}k") 

# a=twoDVector(1,2)
# a.show()

# b=threeDvector(1,2,3)
# b.show()


# Q 02
# class Animals:
#     pass

# class pets(Animals):
#     pass

# class Dog(pets):
    
#     @staticmethod
#     def bark():
#         print("dog is bark")

# d=Dog()
# d.bark()

# Q 03

# class Employee:
#     pass 
    
# e=Employee()
# e.salary=2345
# e.increment=456

# Q 04

# class Employee:
#     def __init__(self):
#         self.salary = 2345
#         self._increment = 456

#     @property
#     def increment(self):
#         return self._increment

#     @increment.setter
#     def increment(self, value):
#         self._increment = value

#     @property
#     def salaryAfterincrement(self):
#         return self.salary + self.salary * (self._increment / 100)

#     @salaryAfterincrement.setter
#     def salaryAfterincrement(self, new_salary):
#         self._increment = ((new_salary / self.salary) - 1) * 100


# # Test
# e = Employee()
# e.salaryAfterincrement = 2800
# print(f"Calculated increment: {e.increment:.2f}%") 



# Q 05

class Complex:
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self):
        sign = "+" if self.i >= 0 else "-"
        return f"{self.r}r {sign} {abs(self.i)}i"

# Test
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)


# Q 06 same to the  Q 1

# Q 07
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

t = Team(["Ali", "Sara", "John"])
print(len(t))  
