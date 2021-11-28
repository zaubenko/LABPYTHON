#Напишите набор простейших классов для создания личных исключений,
# возникающих при работе с объектом типа
# Student (Worker, Pencil, Animal, Cat …, см. л.р. №17, №18).
class Student(Exception):
    def __init__(self, text):
        self.text = text

a = input("Name: ")
try:
    if a == int(a):
        raise Student("You give not str!")
except ValueError:
    print("Error type of value!")
except Student as mr:
    print(mr)
else:
    print(a)