from tkinter import *

val = ""

def btn1():
	global val
	val = val+"1"
	data.set(val)
    
def btn2():
	global val
	val = val+"2"
	data.set(val)
    
def btn3():
	global val
	val = val+"3"
	data.set(val)
    
def btn4():
	global val
	val = val+"4"
	data.set(val)
    
def btn5():
	global val
	val = val+"5"
	data.set(val)
    
def btn6():
	global val
	val = val+"6"
	data.set(val)
    
def btn7():
	global val
	val = val+"7"
	data.set(val)
    
def btn8():
	global val
	val = val+"8"
	data.set(val)
    
    
def btn9():
	global val
	val = val+"9"
	data.set(val)
    
    
def btn0():
	global val
	val = val+"0"
	data.set(val)
    
    
def btnp():
	global val
	val = val+"+"
	data.set(val)
    
    
def btnm():
	global val
	val = val+"-"
	data.set(val)
    
    
def btnmul():
	global val
	val = val+"*"
	data.set(val)
    
def btndiv():
	global val
	val = val+"/"
	data.set(val)
    
def clear():
	global val
	val = ""
	data.set(val)
    
def eq():
	global val
	total = str(eval(val))
	data.set(total)

w = Tk()
w.geometry("250x250")
w.resizable(0,0)

data = StringVar()
lbl = Label(w,text="",textvariable=data)
lbl.pack(expand=True,fill="both")

row1 = Frame(w)
row1.pack(expand=True,fill="both")

row2 = Frame(w)
row2.pack(expand=True,fill="both")

row3 = Frame(w)
row3.pack(expand=True,fill="both")

row4 = Frame(w)
row4.pack(expand=True,fill="both")


btn1 = Button(row1,text="1",command=btn1)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(row1,text="2",command=btn2)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(row1,text="3",command=btn3)
btn3.pack(side=LEFT,expand=True,fill="both")

btnp = Button(row1,text="+",command=btnp)
btnp.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(row2,text="4",command=btn4)
btn4.pack(side=LEFT,expand=True,fill="both")

btn5 = Button(row2,text="5",command=btn5)
btn5.pack(side=LEFT,expand=True,fill="both")

btn6 = Button(row2,text="6",command=btn6)
btn6.pack(side=LEFT,expand=True,fill="both")

btnm = Button(row2,text="-",command=btnm)
btnm.pack(side=LEFT,expand=True,fill="both")

btn7 = Button(row3,text="7",command=btn7)
btn7.pack(side=LEFT,expand=True,fill="both")

btn8 = Button(row3,text="8",command=btn8)
btn8.pack(side=LEFT,expand=True,fill="both")

btn9 = Button(row3,text="9",command=btn9)
btn9.pack(side=LEFT,expand=True,fill="both")

btnmul = Button(row3,text="*",command=btnmul)
btnmul.pack(side=LEFT,expand=True,fill="both")

btnc = Button(row4,text="C",command=clear)
btnc.pack(side=LEFT,expand=True,fill="both")

btn0 = Button(row4,text="0",command=btn0)
btn0.pack(side=LEFT,expand=True,fill="both")

btneq = Button(row4,text="=",command=eq)
btneq.pack(side=LEFT,expand=True,fill="both")

btndiv = Button(row4,text="/",command=btndiv)
btndiv.pack(side=LEFT,expand=True,fill="both")

w.mainloop()

