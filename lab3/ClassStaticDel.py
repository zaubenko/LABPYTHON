#8.	Напишите драйвер к п.7, в котором создается три объекта и на экран выводятся значения обычной и статической переменных членов класса.
# Уничтожьте эти объекты и проследите как будет меняться значение статической переменной члена.#
class StaticDel:
    static=0
    def __init__(self,var,static):
        self.var=var
        self.static=static+1
    def info(self):
        print(self.var,self.static)
    def __del__(self):
        self.static=self.static-1
        print(self.var,self.static)
s1=StaticDel(1,1)
s1.info()
s2=StaticDel(1,2)
s2.info()
s3=StaticDel(1,3)
s3.info()