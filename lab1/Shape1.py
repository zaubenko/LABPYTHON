#3.	Измените классы Shape->Square->Rectangle из предыдущего задания на виртуальные. Для этого добавьте в класс Shape пустые методы для
# вычисления площади и периметра и перекройте их виртуальными методами в производных классах.
# Не забудьте также и про виртуальные деструкторы.
class Shape:
    def __init__(self, color, thickness,length, width):
        self.color = color
        self.thickness = thickness
        self.length = length
        self.width = width
    def Smax(self):
        return (self.length*self.width)
    def Pmax(self):
        return ((self.length*2)+(self.width*2))


class Square(Shape):
    def __init__(self,color, thickness,length,width):
        super().__init__(color,thickness,length,width)
    def S(self):
        return self.Smax()
    def P(self):
        return self.Pmax()

class Rectangle(Square):
    def __init__(self, color, thickness,length,width):
        super().__init__(color, thickness,length,width)
    def S1(self):
        return self.Smax()
    def P1(self):
        return self.Pmax()

Square1=Square("black",1,1,1)
print("Вы создали квадрат. Ваш" , Square1.color, "квадрат имеет периметр - ",Square1.P(),"см", "и площадь - " , Square1.S(), "см")
Rectangle1=Rectangle("red",1,2,3)
print("Вы создали прямоугольник. Ваш" , Rectangle1.color, "прямоугольник имеет периметр - ",Rectangle1.P1(),"см", "и площадь - " , Rectangle1.S1(), "см")
