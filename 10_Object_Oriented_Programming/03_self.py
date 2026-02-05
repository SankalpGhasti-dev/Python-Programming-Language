class Employee:
    language = "py"   
    salary = 2300000
    
    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}.")
    
    @staticmethod

    def greet():
        print("Good Morning !")

sankalp = Employee()

sankalp.greet()

#statice method means method which doesn't take self parameter.

sankalp.getinfo()

# Employee.getinfo(sankalp) The sankalp.getinfo() is internally converted to above line by python interpreter. Here sankalp is passed as self parameter.

