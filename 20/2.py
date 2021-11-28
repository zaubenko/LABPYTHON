#Создайте множество объектов, распечатайте его и выполните в нем поиск.
class firma():
    def __init__(self,position=""):
        self.position=position
    def info(self):
        print(self.position)
positions=["Администратор","Служащий","Рабочий"]
keys=('1','2','3')
persons=[]
b=int(input('''Кого создаём? - 
    0.Админ
    1.Служащий
    2.Рабочий - '''))
person_x=firma(positions[b])
persons.append(person_x.position)


#set
a=set(persons)
print(a)
for value in a:
    name = input("Кого хотим найти ? - ")
    if value == name:
        print(value + " найден")
    else:
        print(value + " не найден")