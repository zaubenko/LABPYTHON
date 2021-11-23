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
class SportCar(Car):
    def __init__(self,horcepower=None):
        super().__init__()
        self.horcepower=horcepower
        self.horcepower=input("Введите количество лошадиных сил спорткара - ")
    def Info(self):
        print("Спорткар" +self.number+" марки "+self.marka+" "+self.data+ " года выпуска " + " имеет на борту " +self.horcepower+ " лошадиных сил и развивает максимальную скорость в " +self.maxspeed+ " километров в час.")
class Wagon(Car):
    def __init__(self,weight=None):
        super().__init__()
        self.weigth=weight
        self.weigth=input("Введите массу вагона - ")
    def Info(self):
        print("Вагон " +self.number+" марки "+self.marka+" "+self.data+ " года выпуска " +" имеет массу " +self.weigth+ " кг и максимальную скорость " +self.maxspeed+ " километров в час." )

class Coupe(Car):
    def __init__(self,roominess=None):
        super().__init__()
        self.roominess=roominess
        self.roominess=input("Вместительный ли багажник? Да/ Нет - ")
        if self.roominess == "Да":
            self.roominess=" вместительный "
        elif self.roominess=="Нет":
            self.roominess=" не очень вместительный "
    def Info(self):
        print("Машина класса Купе " +self.number+" марки "+self.marka+ " "+ self.data+ " года выпуска " +" имеет " +self.roominess+ " багажник и развивает максимальную скорость в " +self.maxspeed+" километров в час.")


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
                3:Микроавтобус
                4:Спорткар
                5:Вагон
                6:Машину класса Купе'''))
if k==1:
    car=Car()
    car.GetInfo()
elif k==2:
    bus=Bus()
    bus.GetInfo2()
elif k==3:
    microbus=MicroBus()
    microbus.GetInfo3()
elif k==4:
    sportcar=SportCar()
    sportcar.Info()
elif k==5:
    wagon=Wagon()
    wagon.Info()
elif k==6:
    coupe=Coupe()
    coupe.Info()
else:
    print("Данного транспортного средства не найдено")