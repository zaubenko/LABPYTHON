#12.	Напишите программу, создающую в цикле несколько объектов этого класса в стеке (свободной памяти).
# Запишите этот объекты последовательно в двоичный файл, пользуясь методами класса
class Transport:
    def __init__(self,number,data,marka):
        self.number=number
        self.data=data
        self.marka=marka
    def info(self):
        return (self.number,self.data,self.marka)
    def write(self):
        h=[self.number,self.data,self.marka]
        f=open("file.bin","ab")
        for i in h:
            k=str(i)
            s=k.encode()
            f.write(s)


x=int(input("Сколько раз делаем запись в файл?"))
for i in range(x):
    a=int(input("number car - "))
    b=input("data car - ")
    c=input("marka car - ")
    t1=Transport(a,b,c)
    t1.write()
    x-=1