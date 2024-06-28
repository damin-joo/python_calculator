import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

from tkinter import *

root = Tk()

#INITIAL SETTINGS
root.title("Calculator Application")
root.resizable(False, False)       # resize (x, y)
root.configure(background='black', padx=10, pady=10)

#FUNCTION
def update(numpad):
    entry.config(state="normal")
    if entry.get() == "0":
        entry.delete(0, END)
    entry.insert(END, numpad)
    entry.config(state="readonly")


def calculate():
    entry.config(state="normal")
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception as err:
        msgbox.showerror("Error", err)
    entry.config(state="readonly")

def clear():
    entry.config(state="normal")
    entry.delete(0, END)
    entry.config(state="readonly")

def percentage():
    entry.config(state="normal")
    to_int = eval(entry.get())
    entry.delete(0, END)
    entry.insert(END, to_int/100)
    entry.config(state="readonly")

def negative():
    entry.config(state="normal")
    if entry.get().startswith("-"):
        entry.delete(0, 1)
    else:
        entry.insert(0, "-")
    entry.config(state="readonly")

#COMBOBOX
##read only enable
opt_read = ["writable", "read-only"]
read_opt = ttk.Combobox(root, state="readonly", values=opt_read, width=10)
read_opt.current(0)
read_opt.grid(row=0, column=3, padx=3, pady=5)

def txt_mode(event):
    selected_item = read_opt.get()
    if (selected_item == "writable"):
        entry.config(state="normal")
    else:
        entry.config(state="readonly")

read_opt.bind("<<ComboboxSelected>>", txt_mode)

#TEXT
entry = Entry(root, font = "Helvetica 20 bold", justify="right")
entry.grid(row=1, sticky=N+E+S+W, columnspan=4, padx=3, pady=3, ipady=8)
entry.insert(0, "0")

#BUTTON
button_name = [
    ["btn_clr", "btn_neg", "btn_perc", "btn_div"], 
    ["btn_7", "btn_8", "btn_9", "btn_mul"], 
    ["btn_4", "btn_5", "btn_6", "btn_sub"], 
    ["btn_1", "btn_2", "btn_3", "btn_add"], 
    ["btn_0", "btn_dot", "btn_eqls"]
]

button_text = [
    ["AC", "+/-", "%", "/"], 
    ["7", "8", "9", "*"], 
    ["4", "5", "6", "-"], 
    ["1", "2", "3", "+"], 
    ["0", ".", "="]
]

for i in range(0, 5):
    for j in range(0, len(button_name[i])):
        text = button_text[i][j]
        name = button_name[i][j]

        if text == "=":
            name = Button(root, text=text, width=10, height=2, command=calculate)
        elif text == "AC":
            name = Button(root, text=text, width=10, height=2, command=clear)
        elif text == "+/-":
            name = Button(root, text=text, width=10, height=2, command=negative)
        elif text == "%":
            name = Button(root, text=text, width=10, height=2, command=percentage)
        else:
            name = Button(root, text=text, width=10, height=2, command=lambda t=text: update(t))

        if text == "0":
            name.grid(row=i+2, column=j, columnspan=2, sticky=N+E+S+W, padx=3, pady=3)
        elif(text == "." or text == "="):
            name.grid(row=i+2, column=j+1, sticky=N+E+S+W, padx=3, pady=3)
        else:
            name.grid(row=i+2, column=j, sticky=N+E+S+W, padx=3, pady=3)


root.mainloop()