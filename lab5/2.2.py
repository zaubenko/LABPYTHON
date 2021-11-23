#7.	Измените программы п.1 и п.2 на циклические.
f=open("text(2).txt", "w")
x=int(input("Сколько ФИО желаете вписать? - " ))
while x!=0:
    a=input("Введите ФИО через пробел - ")
    g=a.split()
    for index in g:
        f.write(index + " ")
    f.write('\n')
    x-=1
f.close()