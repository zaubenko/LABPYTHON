from tkinter import *
def delete():
    selection = languages_listbox.curselection()
    languages_listbox.delete(selection[0])
def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)

root = Tk()
root.title("Города Украины")

language_entry = Entry(width=40)
language_entry.grid(column=0, row=0, padx=6, pady=6)
add_button = Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)

languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=5, pady=5)

languages_listbox.insert(END, "Херсон")
languages_listbox.insert(END, "Николаев")

delete_button = Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()