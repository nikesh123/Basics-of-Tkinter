import tkinter
from tkinter import *
val = ""
A = 0
operator = ""

def result():
    global A
    global operator
    global val
    val2 = (val)
    if(operator=="+"):
        x = int((val2.split("+")[1]))
        res = A + x
        data.set(res)
        
    elif(operator=="-"):
        x = int((val2.split("-")[1]))
        res = A - x
        data.set(res)
        
    elif(operator=="*"):
        x = int((val2.split("*")[1]))
        res = A * x
        data.set(res)
        
    elif(operator=="/"):
        x = int((val2.split("/")[1]))
        res = A/x
        data.set(res)

        
    
        
        
def btn1_click():
    global val
    val = val + "1"
    data.set(val)

def btn2_click():
    global val
    val = val + "2"
    data.set(val)

def btn3_click():
    global val
    val = val + "3"
    data.set(val)

def btnadd_click():
    global A
    global operator
    global val
    A = int(val)
    operator="+"
    val = val + "+"
    data.set(val)
    
def btn4_click():
    global val
    val = val + "4"
    data.set(val)
    
def btn5_click():
    global val
    val = val + "5"
    data.set(val)
    
def btn6_click():
    global val
    val = val + "6"
    data.set(val)
    
def btnsub_click():
    global A
    global operator
    global val
    A = int(val)
    val = val + "-"
    operator = "-"
    data.set(val)
    
def btn7_click():
    global val
    val = val + "7"
    data.set(val)
    
def btn8_click():
    global val
    val = val + "8"
    data.set(val)
    
def btn9_click():
    global val
    val = val + "9"
    data.set(val)
    
def btnmul_click():
    global A
    global operator
    global val
    A = int(val)
    val = val + "*"
    operator = "*"
    data.set(val)
    
def btnC_click():
    global val
    val = ""
    data.set(val)
    
def btn0_click():
    global val
    val = val + "0"
    data.set(val)
    
    
def btndiv_click():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)
    
 
window = Tk()
window.title("Simple Calculator")
data = StringVar()
lbl = Label(window,text="",font=("Verdana",22),textvariable = data, background="#ffffff")
lbl.pack(expand=True,fill="both")


btnrow1 = Frame(window)
btnrow1.pack(expand=True,fill="both")

btnrow2 = Frame(window)
btnrow2.pack(expand=True,fill="both")

btnrow3 = Frame(window)
btnrow3.pack(expand=True,fill="both")

btnrow4 = Frame(window)
btnrow4.pack(expand=True,fill="both")

btn1 = Button(btnrow1,text="1",font=("Verdana",22),relief=GROOVE,border=0,command = btn1_click)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(btnrow1,text="2",font=("Verdana",22),relief=GROOVE,border=0,command=btn2_click)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(btnrow1,text="3",font=("Verdana",22),relief=GROOVE,border=0,command = btn3_click)
btn3.pack(side=LEFT,expand=True,fill="both")

btnadd = Button(btnrow1,text="+",font=("Verdana",22),relief=GROOVE,border=0,command=btnadd_click)
btnadd.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(btnrow2,text="4",font=("Verdana",22),relief=GROOVE,border=0,command=btn4_click)
btn4.pack(side=LEFT,expand=True,fill="both")

btn5 = Button(btnrow2,text="5",font=("Verdana",22),relief=GROOVE,border=0,command=btn5_click)
btn5.pack(side=LEFT,expand=True,fill="both")

btn6 = Button(btnrow2,text="6",font=("Verdana",22),relief=GROOVE,border=0,command=btn6_click)
btn6.pack(side=LEFT,expand=True,fill="both")

btnsub = Button(btnrow2,text="-",font=("Verdana",22),relief=GROOVE,border=0,command=btnsub_click)
btnsub.pack(side=LEFT,expand=True,fill="both")

btn7 = Button(btnrow3,text="7",font=("Verdana",22),relief=GROOVE,border=0,command=btn7_click)
btn7.pack(side=LEFT,expand=True,fill="both")

btn8 = Button(btnrow3,text="8",font=("Verdana",22),relief=GROOVE,border=0,command=btn8_click)
btn8.pack(side=LEFT,expand=True,fill="both")

btn9 = Button(btnrow3,text="9",font=("Verdana",22),relief=GROOVE,border=0,command=btn9_click)
btn9.pack(side=LEFT,expand=True,fill="both")

btnmul = Button(btnrow3,text="*",font=("Verdana",22),relief=GROOVE,border=0,command=btnmul_click)
btnmul.pack(side=LEFT,expand=True,fill="both")

btnC = Button(btnrow4,text="C",font=("Verdana",22),relief=GROOVE,border=0,command=btnC_click)
btnC.pack(side=LEFT,expand=True,fill="both")

btn0 = Button(btnrow4,text="0",font=("Verdana",22),relief=GROOVE,border=0,command=btn0_click)
btn0.pack(side=LEFT,expand=True,fill="both")

btneq = Button(btnrow4,text="=",font=("Verdana",22),relief=GROOVE,border=0,command=result)
btneq.pack(side=LEFT,expand=True,fill="both")

btndiv = Button(btnrow4,text="/",font=("Verdana",22),relief=GROOVE,border=0,command=btndiv_click)
btndiv.pack(side=LEFT,expand=True,fill="both")


window.mainloop()