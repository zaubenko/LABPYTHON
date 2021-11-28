#Создайте ассоциативный список объектов, распечатайте его и выполните в нем поиск.
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


#dict
d = {k: [] for k in keys}
for v in persons:
    d[v].append(v)
print(d)
for value in d.values():
    name=input("Кого хотим найти ? - ")
    if value==name:
        print(value+" найден")
    else:
        print(value+" не найден")



