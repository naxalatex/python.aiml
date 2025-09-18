class Parent:
    def show_family(self):
        return f"this is a parent class"

class Child(Parent):
    def show_family(self):
        return f"this is a child class "

obj1 = Child()
print(obj1.show_family())
