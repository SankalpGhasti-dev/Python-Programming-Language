
class Employee:
    language = "py"   
    salary = 2300000
    


sankalp = Employee()
sankalp.language = "C++"   
print(sankalp.language, sankalp.salary)

# In this case, sankalp.language refers to the instance attribute, which is "C++". and instance attribute takes preference over class attribute. if we don't have instance attribute then it will refer to class attribute.

# When looking for sankalp.attribute, python first checks Is attribute present in object ??
# then, it check is attribute present in class ??
