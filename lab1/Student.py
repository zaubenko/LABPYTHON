#Напишите объявления для следующих диаграмм классов, включив в него члены-данные,
#конструкторы по умолчанию и с параметрами , методы доступа, методы ввода-вывода для клавиатуры и экрана и т.д. :
class Student:
    def __init__(self, number=None, gender=None, surname=None):
        self._number = number
        self._gender = gender
        self._surname = surname
        self._number = input("Введите номер студента - ")
        self._gender = input("Введите пол студента - ")
        self._surname = input("Введите фамилию студента - ")

    def GetInfo(self):
        print("Студент " + self._surname + self._gender + "с номером " + self._number)


class Extramural(Student):
    def __init__(self, job=None, place=None, number=None, gender=None, surname=None):
        super().__init__(number, gender, surname)
        self._job = job
        self._place = place
        self._job = input("Введите место работы студента - ")
        self._place = input("Какую должность занимает студент? - ")

    def GetInfo1(self):
        print("Студент " + self._surname + " " + self._gender + " с номером " + self._number + " работает на " + self._job + " и занимает должность " + self._place)
Sergey = Student()
Sergey.GetInfo()
Sanyok = Extramural()
Sanyok.GetInfo1()


