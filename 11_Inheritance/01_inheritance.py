
class employee:              # It is base/parent class.
    company = "Google"

    def show(self):
        print(f"{self.name} is an Employee and his salary is {self.salary}.")

# class devlopers:
#     company = "Microsoft"

#     def show(self):
#         print(f"{self.name} is an Employee and his salary is {self.salary}.")

#     def showlanguage(self):
#        print(f"{self.name} as a devloper has good command at {self.language} Language.")

# In this program i have made two class. Each stores separate Information about the employee and devloper. consider an case in which we have to store same information about employee and devloper in both class. if the code is big then we asked to edit some information in that class so it will become difficult to edit all the code lines. so to avoid this problem we can use inheritance.

class devlopers(employee):    # It is an child/derived class.

    company = "Microsoft"

    def showlanguage(self):
        print(f"{self.name} as a devloper has good command at {self.language} Language.")
        

a = employee()

b = devlopers()

print(a.company, b.company)  

