import tkinter.ttk as ttk

from tkinter import *

root = Tk()

#INITIAL SETTINGS
root.title("Calculator Application")
root.resizable(False, False)       # resize (x, y)
root.configure(background='black')

#TEXT
num = 0
e = Entry(root, font = "Helvetica 20 bold", justify="right")
e.grid(row=0, sticky=N+E+S+W, columnspan=4, padx=3, pady=3, ipady=8)
e.insert(0, num)

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
        button_name[i][j] = Button(root, text=button_text[i][j], width=5, height=2)

        if(button_text[i][j] == "0"):
            button_name[i][j].grid(row=i+1, column=j, columnspan=2, sticky=N+E+S+W, padx=3, pady=3)
        elif(button_text[i][j] == "."):
            button_name[i][j].grid(row=i+1, column=j+1, sticky=N+E+S+W, padx=3, pady=3)
        elif(button_text[i][j] == "="):
            button_name[i][j].grid(row=i+1, column=j+1, sticky=N+E+S+W, padx=3, pady=3)
        else:
            button_name[i][j].grid(row=i+1, column=j, sticky=N+E+S+W, padx=3, pady=3)


root.mainloop()