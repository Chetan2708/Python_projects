from ast import Num
from math import sqrt
from tkinter import *


def show(n):
    global opr
    opr = var.get()
    if opr == "0":
        opr = ""
    opr = opr + n
    var.set(opr)


def dele():
    global opr
    opr = ""
    var1 = var.get()
    #text.delete(len(var1)-1, END)
    for i in range(0, len(var1)-1):
        opr = opr + var1[i]
    if opr == "":
        opr = "0"
    var.set(opr)


def allclear():
    global opr
    var.set("")
    opr = ""
    if opr == "":
        opr = "0"
    var.set(opr)


def denominator():
    global opr
    opr = ""
    num = var.get()
    num = 1/int(num)
    opr = num
    var.set(opr)


def cancel():
    global opr
    var.set("")
    opr = ""


def equal_to():
    global opr
    equal1 = eval(opr)
    opr = str(equal1)
    var.set(opr)


def plus_minus():
    global opr
    opr = ""
    num = var.get()
    num = int(num) * -1
    opr = num
    var.set(opr)


def square():
    global opr
    opr = ""
    num = var.get()
    num = int(num)**2
    opr = num
    var.set(opr)


def square_root():
    global opr
    opr = ""
    num = var.get()
    num = sqrt(int(num))
    opr = num
    var.set(opr)


root = Tk()
root.geometry("200x180")
root.resizable(width=False, height=False)
root.iconbitmap("cal.ico")
root.title('Python_tkinter_calculator')
var = StringVar()
opr = ""

text = Entry(root, width=25, textvariable=var)
text.grid(row=0, column=0, columnspan=5)
button1 = Button(root, width=5, height=1, text="%",
                 command=lambda: show("%")).grid(row=1, column=1)
button1 = Button(root, width=5, height=1, text="CE",
                 command=lambda: allclear()).grid(row=1, column=2)
button1 = Button(root, width=5, height=1, text="C",
                 command=lambda: cancel()).grid(row=1, column=3)
button1 = Button(root, width=5, height=1, text="del",
                 command=lambda: dele()).grid(row=1, column=4)
button1 = Button(root, width=5, height=1, text="÷",
                 command=lambda: show("/")).grid(row=2, column=4)
button1 = Button(root, width=5, height=1, text="*",
                 command=lambda: show("*")).grid(row=3, column=4)
button1 = Button(root, width=5, height=1, text="-",
                 command=lambda: show("-")).grid(row=4, column=4)
button1 = Button(root, width=5, height=1, text="+",
                 command=lambda: show("+")).grid(row=5, column=4)
button1 = Button(root, width=5, height=1, text="1",
                 command=lambda: show("1")).grid(row=5, column=1)
button1 = Button(root, width=5, height=1, text="2",
                 command=lambda: show("2")).grid(row=5, column=2)
button1 = Button(root, width=5, height=1, text="3",
                 command=lambda: show("3")).grid(row=5, column=3)
button1 = Button(root, width=5, height=1, text="4",
                 command=lambda: show("4")).grid(row=4, column=1)
button1 = Button(root, width=5, height=1, text="5",
                 command=lambda: show("5")).grid(row=4, column=2)
button1 = Button(root, width=5, height=1, text="6",
                 command=lambda: show("6")).grid(row=4, column=3)
button1 = Button(root, width=5, height=1, text="7",
                 command=lambda: show("7")).grid(row=3, column=1)
button1 = Button(root, width=5, height=1, text="8",
                 command=lambda: show("8")).grid(row=3, column=2)
button1 = Button(root, width=5, height=1, text="9",
                 command=lambda: show("9")).grid(row=3, column=3)
button1 = Button(root, width=5, height=1, text="0",
                 command=lambda: show("0")).grid(row=6, column=2)
button1 = Button(root, width=5, height=1, text="=",
                 command=lambda: equal_to()).grid(row=6, column=4)
button1 = Button(root, width=5, height=1, text=".",
                 command=lambda: show(".")).grid(row=6, column=3)
button1 = Button(root, width=5, height=1, text="+/-",
                 command=lambda: plus_minus()).grid(row=6, column=1)
button1 = Button(root, width=5, height=1, text="1/x",
                 command=lambda: denominator()).grid(row=2, column=1)
button1 = Button(root, width=5, height=1, text="x²",
                 command=lambda: square()).grid(row=2, column=2)
button1 = Button(root, width=5, height=1, text="√x ",
                 command=lambda: square_root()).grid(row=2, column=3)
root.mainloop()
