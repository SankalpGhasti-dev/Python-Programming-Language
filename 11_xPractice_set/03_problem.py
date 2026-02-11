class employee: 
    salary = 10000
    increment = 20
    
    
    @property
    def salaryAfterIncrement(self):
            return (self.salary + self.salary * (self.increment/100))
    
    @increment.setter
    def increment(self, salary):
          

a = employee()
print(a.salaryAfterIncrement) 
