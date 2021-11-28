# •	Элементы управления: флажки, радиокнопки, статические элементы

from tkinter import *

phones = [("iPhone", 1), ("Samsung", 2), ("Huawei", 3), ("Motorolla", 4)]


def select():
    l = phone.get()
    if l == 1:
        sel.config(text="Выбран iPhone")
    elif l == 2:
        sel.config(text="Выбран Samsung")
    elif l == 3:
        sel.config(text="Выбран Huawei")
    elif l == 4:
        sel.config(text="Выбрана Motorolla")


root = Tk()
root.title("Демонстрация RadioButton")
root.geometry("300x300")

header = Label(text="Какой телефон предпочитаете?", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

phone = IntVar()

row = 1
for txt, val in phones:
    Radiobutton(text=txt, value=val, variable=phone, padx=15, pady=10, command=select) \
        .grid(row=row, sticky=W)
    row += 1

sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)

root.mainloop()