#3.	Напишите программу, в которой классы Car и Bus будут производными от класса Transport, а MicroBus – производным от  Car и Bus.
# Сделайте Transport абстрактным типом данных с двумя чисто виртуальными функциями. Классы Car и Bus не должны быть ADT.
# Проверьте программу, путем создания объектов разных типов
class Transport:
    def __init__(self,number=None,data=None,marka=None):
        self.number=number
        self.data=data
        self.marka=marka
        self.number=input("Введите номер транспорта - ")
        self.data=input("Введите год выпуска данного транспорта - ")
        self.marka=input("Введите марку транспорта - ")

class Car(Transport):
    def __init__(self,maxspeed=None,number=None,data=None,marka=None):
        super().__init__(number, data, marka)
        self.maxspeed=maxspeed
        self.maxspeed=input("Введите максимальную скорость машины - ")
    def GetInfo(self):
        print(
            "Автомобиль " + self.number + " марки " + self.marka + " " + self.data + " года выпуска " + " имеет максимальную скорость " + self.maxspeed + " километров в час ")



class Bus(Transport):
    def __init__(self,count=None,number=None,data=None,marka=None):
        super().__init__(number,data,marka)
        self.count=count
        self.count=input("Введите количесто посадочных мест в автобусе - ")
    def GetInfo2(self):
        print("Автобус " + self.number + " марки " + self.marka + " " + self.data + " года выпуска " + " имеет максимальное количество посадочных мест в размере " + self.count + " мест ")

class MicroBus(Car,Bus):
    def __init__(self,count=None,number=None,data=None,marka=None, maxspeed=None):
        super(MicroBus,self).__init__(maxspeed)
        Bus.__init__(self,count)
        self.number=number
        self.data=data
        self.marka=marka
    def GetInfo3(self):
        print("Микроавтобус " + self.number + " марки " + self.marka + " " + self.data + " года выпуска " + " имеет максимальное количество посадочных мест в размере " + self.count + "и иимеет максимальную скорость " +
              self.maxspeed + " километров в час ")

k=int(input('''Что вы хотите создать?
                1:Машина
                2:Автобус
                3:Микроавтобус'''))
if k==1:
    car=Car()
    car.GetInfo()
elif k==2:
    bus=Bus()
    bus.GetInfo2()
elif k==3:
    microbus=MicroBus()
    microbus.GetInfo3()
else:
    print("Данного транспортного средства не найдено")