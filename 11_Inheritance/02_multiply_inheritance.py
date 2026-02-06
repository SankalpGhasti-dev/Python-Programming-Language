
class employee:              # It is base/parent class.
    company = "Google"
    name = "sankalp"
    salary = 1000000

    def show(self):
        print(f"{self.name} is an Employee and his salary is {self.salary}.")


class coder:
    language = "python"

    def showlanguage(self):
        print(f"out of all the languages here is your language: {self.language}.")


class devlopers(employee, coder):    # It is an child/derived class.

    company = "Microsoft"

    def showlanguage(self):
        print(f"{self.name} as a devloper has good command at {self.language} Language.")
        

a = employee()

b = coder()

c = devlopers()

c.show()
c.showlanguage()

# here devlopers are employee as well as coder. so we can access the properties of both class in devlopers class. this is called multiple inheritance.
