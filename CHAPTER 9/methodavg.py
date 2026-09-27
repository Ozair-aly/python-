class Student:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def average(self):
        return (self.num1 + self.num2 + self.num3) / 3

s1 = Student(34, 67, 76)
print(s1.average())