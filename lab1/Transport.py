class Transport:
    def __init__(self,number=None,data=None,marka=None):
        self._number=number
        self._data=data
        self._marka=marka
        self._number=input("Введите номер транспорта - ")
        self._data=input("Введите год выпуска данного транспорта - ")
        self._marka=input("Введите марку транспорта - ")
    def GetInfo(self):
        print("Транспорт " + self._marka + " выпущен в " + self._data + " году")

class Car(Transport):
    def __init__(self,maxspeed=None,number=None,data=None,marka=None):
        super().__init__(number,data,marka)
        self._maxspeed=maxspeed
        self._maxspeed=input("Введите максимальную скорость машины - ")
    def GetInfo1(self):
        print("Автомобиль " + self._number + " марки " + self._marka + " " + self._data + " года выпуска " + " имеет максимальную скорость " + self._maxspeed + " километров в час ")

class Bus(Transport):
    def __init__(self,count=None,number=None,data=None,marka=None):
        super().__init__(number,data,marka)
        self._count=count
        self._count=input("Введите количесто посадочных мест в автобусе - ")
    def GetInfo2(self):
        print("Автобус " + self._number + " марки " + self._marka + " " + self._data + " года выпуска " + " имеет максимальное количество посадочных мест в размере " + self._count + " мест ")
Transport1=Transport()
Transport1.GetInfo()
Car1=Car()
Car1.GetInfo1()
Bus1=Bus()
Bus1.GetInfo2()