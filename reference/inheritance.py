class rocks:
    def __init__(self):
        print("this is basalt rock")

class stone(rocks):
    def __init__(self):
       super().__init__()
print("this is limestone")

class things :
    def __init__(self,stool,chair):
        self.stool = stool
        self.chair = chair
        print("this is a stool")

class solids(things):
    def __init__(self,stool, chair):
        super().__init__(stool,chair)
        self.chair = chair
        print("this is a chair")
A = solids("chair","stool")

