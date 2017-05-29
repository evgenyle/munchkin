from tkinter import *
import random
ryad1 = "* \t *"
ryad2 = "* \t "
ryad3 = " \t *"
ryad4 = " *  "
ryad5 = "   "


def dice_result(event):
    x = random.randint(1,6)
    if x == 1:
        lab1["text"] = ryad5
        lab2["text"] = ryad4
        lab3["text"] = ryad5
    elif x == 2:
        lab1["text"] = ryad2
        lab2["text"] = ryad5
        lab3["text"] = ryad3	
    elif x == 3:
        lab1["text"] = ryad2
        lab2["text"] = ryad4
        lab3["text"] = ryad3
    elif x == 4:
        lab1["text"] = ryad1
        lab2["text"] = ryad5
        lab3["text"] = ryad1
    elif x == 5:
        lab1["text"] = ryad1
        lab2["text"] = ryad4
        lab3["text"] = ryad1
    elif x == 6:
        lab1["text"] = ryad1
        lab2["text"] = ryad1
        lab3["text"] = ryad1		


root = Tk()

lab1 = Label (root)
lab2 = Label (root)
lab3 = Label (root)

but = Button(root, text = "Dice me!")
but.bind("<Button-1>", dice_result)




lab1.pack()
lab2.pack()
lab3.pack()
but.pack()

root.mainloop()