
class employee:              # It is base/parent class.
    company = "Google"
    name = "sankalp"
    salary = 1000000

    def show(self):
        print(f"{self.name} is an Employee and his salary is {self.salary}.")


class coder(employee):
    language = "python"

    def showlanguage(self):
        print(f"out of all the languages here is your language: {self.language}.")


class devlopers(coder):    # It is an child/derived class.

    company = "Microsoft"

    def showlanguage(self):
        print(f"{self.name} as a devloper has good command at {self.language} Language.")
        

a = employee()

b = coder()

c = devlopers()

c.show()
c.showlanguage()

# here we have created employee class after that we have created coder class which is child class of employee class and after that we have created devlopers class which is child class of coder class. so devlopers class is a child class of coder class and coder class is a child class of employee class. so we can access the properties of both class in devlopers class. this is called multilevel inheritance.
