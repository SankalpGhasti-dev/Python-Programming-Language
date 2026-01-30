class Employee:
    language = "py"   # This is a class attribute
    salary = 2300000
    


sankalp = Employee()
sankalp.name = "Sankalp"   # This is an instance attribute (object attribute)
print(sankalp.name, sankalp.language, sankalp.salary)

soham = Employee()
soham.name = "Soham"
print(soham.name, soham.salary, soham.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to class.
