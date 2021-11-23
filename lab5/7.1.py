#17.	Запустите программу п.2 так, чтобы она выводила свои результаты не на экран, а в текстовый файл.
import re
r = re.compile("[а-яА-Я-]+")
t=input("Введите точное имя файла с расширением txt - ")
if t!="text(7).txt":
    print("error")
    exit()
else:
    f = open(t, "r")
    russian = [w for w in filter(r.match, f.read())]
    f.close()
    f=open(t,"w")
    for i in russian:
        f.write("%s\n" % i)
