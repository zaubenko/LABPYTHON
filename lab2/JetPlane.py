class Rocket:
    def __init__(self,length=None):
        self.length=length
        self.length=input("введите длину корпуса от ракеты - ")
class Airplane:
    def __init__(self,color=None):
        self.color=color
        self.color=input("введите цвет корпуса от самолёта - ")
class JetPlane(Rocket,Airplane):
    def __init__(self,speed=None,length=None,color=None):
        super(JetPlane,self).__init__(length)
        Airplane.__init__(self, color)
        self.speed=speed
        self.speed=input("введите максимальную скорость нового реактивного самолёта - ")
    def GetInfo(self):
        print("Новосозданный реактивный самолёт имеет " +self.color+ " цвет и длину корпуса " + self.length + " м. Имеет максимальную скорость " +self.speed+ " километров в час ")
Groza=JetPlane()
Groza.GetInfo()
