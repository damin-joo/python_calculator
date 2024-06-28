import tkinter.ttk as ttk

from tkinter import *

root = Tk()

#INITIAL SETTINGS
root.title("Calculator Application")
root.resizable(False, False)       # resize (x, y)
root.configure(background='black')

#TEXT
entry = Entry(root, font = "Helvetica 20 bold", justify="right")
entry.grid(row=0, sticky=N+E+S+W, columnspan=4, padx=3, pady=3, ipady=8)
entry.insert(0, "0")

#FUNCTION
def update(numpad):
    print(entry.get())
    if entry.get() == "0":
        entry.delete(0, END)
    entry.insert(END, numpad)

#BUTTON
button_name = [
    ["btn_clr", "btn_neg", "", "btn_div"], 
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

        name = Button(root, text=text, width=5, height=2, command=lambda t=text: update(t))

        if(text == "0"):
            name.grid(row=i+1, column=j, columnspan=2, sticky=N+E+S+W, padx=3, pady=3)
        elif(text == "." or text == "="):
            name.grid(row=i+1, column=j+1, sticky=N+E+S+W, padx=3, pady=3)
        else:
            name.grid(row=i+1, column=j, sticky=N+E+S+W, padx=3, pady=3)


root.mainloop()