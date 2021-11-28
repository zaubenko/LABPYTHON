#Напишите функции-шаблоны  для :
#удваивания значения объекта любого типов;
# обмена значений двух объектов любых типов;
#определения большего из значений двух объектов любых типов;
#сравнения значений двух объектов любых типов.

class Obj():
    def __init__(self,var=None,var1=None):
        self.var=var
        self.var1=var1
    def up(self):
        self.var=self.var*2
        print(self.var)
    def conf(self):
        self.var,self.var1=self.var1,self.var
        print(self.var,self.var1)
    def por(self):
        if self.var>self.var1:
            print(self.var)
        else:
            print(self.var1)
    def ifelse(self):
        if self.var>self.var1:
            print("var>var1")
        elif self.var==self.var1:
            print("self.var==self.var1")
        else:
            print("var1>var")

objects=Obj(1,3)
def up():
    objects.up()
def conf():
    objects.conf()
def por():
    objects.por()
def ifelse():
    objects.ifelse()
print('''Какую функцию шаблон хотите использовать для объекта? - 

                            1.Удвоение
                            2.Смена значений
                            3.Определение большего
                            4.Сравнение''')
x=int(input())
if x==1:
    up()
elif x==2:
    conf()
elif x==3:
    por()
elif x==4:
    ifelse()
else:
    print("Error")

