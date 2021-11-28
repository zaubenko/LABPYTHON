#Измените ранее разработанный класс на класс внутри пространства имен.
def namespace():
    class Student:
        def __init__(self, name):
            self.name=name

        def check(self):
            if self.name == str(self.name):
                return True
    name=input()
    s = Student(name)
    s.check()
    if s.check() != True:
        status = False
    else:
        status = True
    print(status)

    return Student
namespace()
