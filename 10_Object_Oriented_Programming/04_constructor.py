
class Employee:
    language = "py"   
    salary = 2300000

    # def function which is automatically called when we create an object is called constructor. It also known as dunder method because it has double underscores before and after the name. The name of the constructor is __init__.

    def __init__(self, name, salary, language):
        
        print("I am creating an object.")
        self.name = name
        self.salary = salary
        self.language = language

    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}.")
    
    @staticmethod

    def greet():
        print("Good Morning !")

# while creating an object we have to pass the attributes which are defined in the constructor. If we don't pass the attributes then we will get an error.

sankalp = Employee("Sankalp", 200000, "Javascript")

print(sankalp.name, sankalp.salary, sankalp.language) 

