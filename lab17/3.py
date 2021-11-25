#•	Элементы управления: списки, поля ввода

from tkinter import *
def delete():
    selection = city_listbox.curselection()
    city_listbox.delete(selection[0])
def add():
    new_city = city_entry.get()
    city_listbox.insert(0, new_city)
root = Tk()
root.title("Города Украины")

city_entry = Entry(width=40)
city_entry.grid(column=0, row=0, padx=6, pady=6)
add_button = Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)

city_listbox = Listbox()
city_listbox.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=5, pady=5)

city_listbox.insert(END, "Херсон")
city_listbox.insert(END, "Николаев")

delete_button = Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)
sel = Label(padx=15, pady=10)


root.mainloop()