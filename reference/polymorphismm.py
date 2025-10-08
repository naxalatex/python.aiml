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


                     