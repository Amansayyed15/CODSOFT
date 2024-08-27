from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Calculator")

global resultnum
resultnum = 0

def sumnumber():
    global resultnum
    resultnum = int(firstnumber.get()) + int(secondnumber.get())
    result_label.config(text=resultnum) 
def subtractnum():
    global resultnum
    resultnum = int(firstnumber.get()) - int(secondnumber.get())
    result_label.config(text=resultnum) 
def mulnumber():
    global resultnum
    resultnum = int(firstnumber.get()) * int(secondnumber.get())
    result_label.config(text=resultnum) 
def divnumber():
    global resultnum
    resultnum = int(firstnumber.get()) / int(secondnumber.get())
    result_label.config(text=resultnum) 



Label(root, text="Enter your first number").grid(row=1, column=1)
firstnumber = StringVar()
firstentry = Entry(root, textvariable=firstnumber)
firstentry.grid(row=1, column=2)

Label(root, text="Enter your second number").grid(row=2, column=1)
secondnumber = StringVar()
secondentry = Entry(root, textvariable=secondnumber)
secondentry.grid(row=2, column=2)

addbtn = Button(root, text="+", command=sumnumber)
addbtn.grid(row=3, column=1)
subbtn = Button(root, text="-", command=subtractnum)
subbtn.grid(row=3, column=2)
mulbtn = Button(root, text="*", command=mulnumber)
mulbtn.grid(row=4, column=1)
divbtn = Button(root, text="/", command=divnumber)
divbtn.grid(row=4, column=2)

Label(root, text="Results:").grid(row=5, column=1)
result_label = Label(root, text=str(resultnum)) 
result_label.grid(row=5, column=2)

root.mainloop()
