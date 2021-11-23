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
class B747(JetPlane):
    def __init__(self,weapon=None):
        super(B747, self).__init__()
        self.weapon=weapon
        self.weapon=input("введите название вооружения установленного на данный аппарат - ")
    def GetInfo(self):
        print("Новосозданный реактивный самолёт имеет " +self.color+ " цвет и длину корпуса " + self.length + " м. Имеет максимальную скорость " + self.speed + " километров в час. На борту B747 был установлен " +self.weapon)
b747=B747()
b747.GetInfo()
