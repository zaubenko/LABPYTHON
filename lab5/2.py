#5.	Напишите программу, предлагающую пользователю ввести его фамилию, имя и отчество , а затем выводящую эти сведения в текстовый файл
f=open("text(2).txt", "w")
a=input("Введите ФИО через пробел - ")
x=a.split()
for index in x:
    f.write(index + '\n')
f.close()