#9.	Сделайте статическую переменную п.7-8 приватной.
# Напишите и используйте статическую функцию-член для доступа к приватной статической переменной члену?#
class StaticDel:
    static=0
    def __init__(self,var,static):
        self.var=var
        self._static=static+1
    def info_private(self):
        print(self.var,self._static)
    def __del__(self):
        self._static=self._static-1
        print(self.var,self._static)
s1=StaticDel(1,1)
s1.info_private()
s2=StaticDel(1,2)
s2.info_private()
s3=StaticDel(1,3)
s3.info_private()
