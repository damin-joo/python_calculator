from tkinter import *

root = Tk()

#INITIAL SETTINGS
root.title("Calculator Application")
root.geometry("320x480+350+200")        # w x h + x + y
root.resizable(False, False)       # resize (x, y)

#BUTTON
button_name = [
    ["btn_f16", "btn_f17", "btn_f18", "btn_f19"], 
    ["btn_clr", "btn_eql", "btn_div", "btn_mul"], 
    ["btn_7", "btn_8", "btn_9", "btn_sub"], 
    ["btn_4", "btn_5", "btn_6", "btn_add"], 
    ["btn_1", "btn_2", "btn_3", "btn_enter"], 
    ["btn_0", "btn_dot"]
]
button_text = [
    ["F16", "F17", "F18", "F19"], 
    ["clear", "=", "/", "*"],
    ["7", "8", "9", "-"], 
    ["4", "5", "6", "+"], 
    ["1", "2", "3", "enter"], 
    ["0", "."]
]

for i in range(0, 6):
    for j in range(0, len(button_name[i])):
        button_name[i][j] = Button(root, text=button_text[i][j], width=5, height=2)

        if(button_text[i][j] == "enter"):
            button_name[i][j].grid(row=4, column=3, rowspan=2, sticky=N+E+S+W, padx=3, pady=3)
        elif(button_text[i][j] == "0"):
            button_name[i][j].grid(row=5, column=0, columnspan=2, sticky=N+E+S+W, padx=3, pady=3)
        elif(button_text[i][j] == "."):
            button_name[i][j].grid(row=5, column=2, sticky=N+E+S+W, padx=3, pady=3)
        else:
            button_name[i][j].grid(row=i, column=j, sticky=N+E+S+W, padx=3, pady=3)

"""
#row1
btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

#row2
btn_clr = Button(root, text="clear", width=5, height=2)
btn_eql = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

#row3
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

#row4
btn4 = Button(root, text="4", width=5, height=2)
btn5 = Button(root, text="5", width=5, height=2)
btn6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

#row5
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

#row6
btn_0 = Button(root, text="0", width=5, height=2)
btn_dot = Button(root, text=".", width=5, height=2)

"""

"""
#GRID
##row1
btn_f16.grid(row=0, column=0, sticky=N+E+S+W, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+S+W, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+S+W, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+S+W, padx=3, pady=3)

#row2
btn_clr.grid(row=1, column=0, sticky=N+E+S+W, padx=3, pady=3)
btn_eql.grid(row=1, column=1, sticky=N+E+S+W, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+S+W, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+S+W, padx=3, pady=3)

#row3
btn_7.grid(row=2, column=0, sticky=N+E+S+W, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+S+W, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+S+W, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+S+W, padx=3, pady=3)

#row4
btn4.grid(row=3, column=0, sticky=N+E+S+W, padx=3, pady=3)
btn5.grid(row=3, column=1, sticky=N+E+S+W, padx=3, pady=3)
btn6.grid(row=3, column=2, sticky=N+E+S+W, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+S+W, padx=3, pady=3)

#row5
btn_1.grid(row=4, column=0, sticky=N+E+S+W, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+S+W, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+S+W, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+S+W, padx=3, pady=3)

#row6
btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+S+W, padx=3, pady=3)
btn_dot.grid(row=5, column=2, sticky=N+E+S+W, padx=3, pady=3)
"""

root.mainloop()