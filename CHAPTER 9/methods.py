class Student:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def highest(self):
        high = self.num1
        if self.num2 > high:
            high = self.num2
        if self.num3 > high:
            high = self.num3
            return high

            

s1 = Student(34 ,67 ,76)
print(s1.highest())
