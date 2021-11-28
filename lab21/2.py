# Измените конструкторы, методы доступа типа set, метод ввода с клавиатуры так,
# чтобы они вызывали инвариаты класса и выбрасывали (throw)
# исключения в случае приема неправильных данных для объекта.
class Student(Exception):
    def __init__(self,name='name'):
        self.name = name
a = input("Name- ")
age=input('Age')
def greet(name: str) -> str:
    return 'Hello ' + name
try:
    if a == int(a):
        raise Student("You give not str!")
except ValueError:
    print("Error type of value!")
except Student as mer:
    print(mer)
else:
    print(a)
    print(greet(age))