#	Напишите дружественную функцию для обработки объекта типа фирма.
#	Напишите главную программу, выполняющую создание и обработку  объекта типа фирма.
class firma():
    def __init__(self,position=""):
        self.position=position
    def info(self):
        print(self.position)
positions=["Администратор","Служащий","Рабочий"]
persons=[]
b=int(input('''Кого создаём? - 
    0.Админ
    1.Служащий
    2.Рабочий - '''))
person_x=firma(positions[b])
persons.append(person_x.position)
print(persons)
def FooFriend():
    print("Кто получит отпуск в следующем месяце? - ")
    print(persons)
    x=int(input("введите индекс обьекта - "))
    persons[x]=persons[x]+" в отпуске"
    print(persons[x])
FooFriend()

person_x.info()