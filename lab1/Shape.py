#Напишите объявление класса Rectangle (прямоугольник), который является производным от Square (квадрат), который, в свою очередь – производный от Shape(фигура).
# В классе Shape объявите следующие защищенные члены-данные : цвет линий фигуры и толщина ее линий  и напишите 2 конструктора - по умолчанию и с параметрами.
# В классах Square и Rectangle объявите закрытые (защищенные)  члены-данные для хранения размеров каждой из фигур, несколько конструкторов, вызывающих конструкторы базового класса, а также методы для вычисления площади и периметра фигур.
# В классе Rectangle обязательно используйте перекрывание методов базового класса Square.
# При необходимости добавьте в классы  методы доступа. Напишите главную программу, в которой выполните создание объектов-фигур различных типов и их обработку.
class Shape:
    def __init__(self, color="red", thickness=111):
        self._color = color
        self._thickness = thickness

class Square(Shape):
    def __init__(self, side, color, thickness):
        super().__init__(color,thickness)
        self._side = side
    def S(self):
        return(self._side*self._side)
    def P(self):
        return (self._side*4)

class Rectangle(Square):
    def __init__(self, length, width, color, thickness):
        super(Shape,self).__init__(color, thickness)
        self._length = length
        self._width = width
    def S1(self):
        return (self._length*self._width)
    def P1(self):
        return ((self._length*2)+(self._width*2))

Square1=Square(1, "black",1)
print("Вы создали квадрат. Ваш" , Square1._color, " квадрат имеет периметр - ",Square1.P()," см ", " и площадь - " , Square1.S(), " см")
Rectangle1=Rectangle(1,2,"red",3)
print("Вы создали прямоугольник. Ваш" , Rectangle1._color, "прямоугольник имеет периметр - ",Rectangle1.P1()," см ", " и площадь - " , Rectangle1.S1(), " см")
