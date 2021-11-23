#9.	Используйте  любой ранее разработанный класс. Напишите программу, создающую в цикле несколько объектов этого класса в стеке (свободной памяти).
# Запишите этот объекты в двоичный файл
class Transport:
    def __init__(self,number,data,marka):
        self.number=number
        self.data=data
        self.marka=marka
    def info(self):
        return (self.number,self.data,self.marka)

x=int(input("Сколько раз делаем запись в файл?"))
h=open("file.bin","w")
for i in range(x):
    a=input("number car - ")
    b=input("data car - ")
    c=input("marka car - ")
    t1=Transport(a,b,c)
    k = [str(t1.info())]
    for g in k:
        h.write(g)
    h.close()
    x-=1
