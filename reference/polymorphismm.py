class Parent:
    def show_family(self):
        return f"this is a parent class"

class Child(Parent):
    def show_family(self):
        return f"this is a child class "

obj1 = Child()
print(obj1.show_family())

#Create a base class Employee with the following: 1.Attributes : emp_id, name, and private attribute __salary Methods :

#a).set_salary(amount) → sets the salary (should not accept negative values)
#b). get_salary() → returns the salary

#2.Create subclasses Developer and Manager with their own role attribute.
#3. Print each employee's name, role, and salary.


class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.__salary = salary

    def set_salary(self,amount):
        if amount < 0 :
            print("value cannot be negative")
        else:
            self.__salary = amount
    
    def get_salary(self):
        return self.__salary

class Developer(Employee):
    def __init__(self, emp_id, name, salary, role):
        super().__init__(emp_id, name, salary)
        self.role = role

    def show_details(self):
        return f" name: {self.name}, role: {self.role} salary: {self.get_salary()}"



class Manager(Employee):
    def __init__(self, emp_id, name, salary, role):
        super().__init__(emp_id,name,salary)
        self.role = role
    
    def show_details(self):
        return f"name :{self.name}, role:{self.role} salary: {self.get_salary()}"

obj1 = Developer(7025,"sidharth",90000,"AI Engineer")
obj2 = Manager(997248,"frida", 120000,"branch")
print(obj1.show_details())
print(obj2.show_details())
obj1.set_salary(100000)
print(obj1.show_details())
obj2.set_salary(130000)
print(obj2.show_details())
