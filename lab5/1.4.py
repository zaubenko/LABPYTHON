#4.	Используя один из ранее разработанных классов (Worker, Student … ), создайте в программе список объектов путем ввода данных с клавиатуры и рап
# ечатайте его на экране в виде таблицы.



class Student:
    def __init__(self, surname=None, age=None, salary=None):
        self._surname = surname
        self._age = age
        self._salary = salary
        self._surname = input("Введите фамилию студента - ")
        self._age = input("Введите возраст студента - ")
        self._salary = input("Введите зарплату студента - ")

    def GetInfo(self):
        print(" "*2,"1."," "*6, self._surname, " "*(22-len(self._surname)), self._age, " "*18, self._salary,"\n", "-"*70)
s=Student()
print("-"*72, "\n", "№"," "*3, ":", " "*3, "Фамилия", " "*5, ":", " "*5, "Возраст", " "*5, ":", " "*5, "Зарплата", "\n", "-"*70)
s.GetInfo()