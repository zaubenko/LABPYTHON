#•	Обработка сообщений
#	Окна сообщений, ресурсы, меню и акселераторы
# •	Модальные и немодальные диалоговые окна
from tkinter import *
from tkinter import messagebox


def display_full_name():
    messagebox.showinfo("Добро пожаловать " + name.get() + " " + surname.get())


root = Tk()
root.title("Python")

name = StringVar()
surname = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

message_button = Button(text="ADD", command=display_full_name)
message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()