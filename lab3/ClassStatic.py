#7.	Напишите небольшую программу с объявлением класса, имеющего одну переменную-член  и одну статическую переменную-член.
# Пусть конструктор инициализирует переменную-член и инкрементирует статическую переменную член, а деструктор – декрементирует ее.#
class Static:
    static=0
    def __init__(self,var,static):
        self.var=var
        self.static=static+1
    def __del__(self):
        self.static=self.static-1
        print(self.static,self.var)

s=Static(1,1)


