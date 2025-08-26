
# OPP in python


class Employee:
    Language="python"
    salary=1200000 
    
    def __init__(self,name,Salary,language):
        self.name=name
        self.salary=Salary
        self.Language=language
        print("I am creating an object ")
         
    def getinfo(self):
        print(f"the language is {self.Language} and salary is {self.salary}")
     
     
    def greet():
        print("Hello Ansir") 
    
    
    # this belo code work like the mai class like in java
Ansir=Employee("Ansir",120000,"Java")
Ansir.name="baba"
print(Ansir.name, Ansir.Language, Ansir.salary)
Ansir.getinfo()
# Employee.getinfo(Ansir)      ---> both work same   