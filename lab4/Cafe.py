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
