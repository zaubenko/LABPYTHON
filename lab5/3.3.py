#7.	Измените программы п.1 и п.2 на циклические.
with open("text1(3).txt", "r") as f:
    x = int(input("Сколько ФИО желаете вывести на экран ? - "))
    while x != 0:
        content=f.readline()
        print(content)
        x-=1
f.close()
