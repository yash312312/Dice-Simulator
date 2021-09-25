from tkinter import *
import random

root = Tk()

root.geometry("250x150")
root.eval('tk::PlaceWindow . center')
# root.maxsize(112, 150)
root.title("Dice Simulator")

photo = PhotoImage(file="static/dice0.png")


def roll_dice():
    global photo
    num = random.randint(1, 6)
    s = "static/dice" + str(num) + ".png"
    photo = PhotoImage(file=s)
    l1.config(image=photo)
    print('\t', num)


l1 = Label(root, image=photo)
l1.pack()

b1 = Button(root, text="Roll", borderwidth=8, fg="black", command=roll_dice)
b1.pack()

root.mainloop()
