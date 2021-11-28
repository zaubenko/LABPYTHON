#Напишите в классе Student метод-инвариант класса.
class Student:
    def __init__(self,name=None):
        self.name=name
    def check(self):
        if self.name==str(self.name):
            return True
name=input()
s=Student(name)
s.check()
if s.check()!=True:
    status=False
else:
    status=True
print(status)