class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def show_calculation(self):
        return f"this is a arithimetic operation"

object1 = Calc(6,7)
print(object1.add())
print(object1.show_calculation())