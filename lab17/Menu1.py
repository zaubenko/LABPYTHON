import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not path:
        return
    txt_edit.delete(1.0, tk.END)
    with open(path, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Редактор текста v1.0 - {path}")

def save_file():
    path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not path:
        return
    with open(path, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Редактор текста v1.0 - {path}")

window = tk.Tk()
window.title("Редактор Текста v1.0")
window.rowconfigure(0, minsize=1920, weight=1)
window.columnconfigure(1, minsize=1080, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file)
btn_save = tk.Button(fr_buttons, text="Сохранить как", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()