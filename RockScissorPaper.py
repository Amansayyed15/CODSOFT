import random
from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Rock Paper N Scissors Game")

choice = [1,2,3]

def rock():
    computerplay = random.choice(choice)
    myplay = 1
    print(computerplay)
    if(myplay==computerplay):
        result.config(text="Computer's Play is Rock so its a Draw")
    elif(computerplay==2):
        result.config(text="Computer's Play is Paper so you loose")
    elif(computerplay==3):
        result.config(text="Computer's Play is Scissor so you Won")
    
def paper():
    computerplay = random.choice(choice)
    myplay = 2
    print(computerplay)
    if(myplay==computerplay):
        result.config(text="Computer's Play is Rock so you Won")
    elif(computerplay==2):
        result.config(text="Computer's Play is Paper so its a Draw")
    elif(computerplay==3):
        result.config(text="Computer's Play is Scissor so you Loose")

def scissor():
    computerplay = random.choice(choice)
    myplay = 3
    print(computerplay)
    if(myplay==computerplay):
        result.config(text="Computer's Play is Rock so you Loose")
    elif(computerplay==2):
        result.config(text="Computer's Play is Paper so you Won")
    elif(computerplay==3):
        result.config(text="Computer's Play is Scissor so its a Draw")
    
        

Label(root,text="Choose one of the following:",font="helvica 15 bold").grid(row=1,column=1,padx=55,pady=15)

rockbtn = Button(root,text="Rock",command=rock)
rockbtn.grid(row=2,column=1,padx=5,pady=5)

paperbtn = Button(root,text="Paper",command=paper)
paperbtn.grid(row=3,column=1,padx=5,pady=5)

scissorbtn = Button(root,text="Scissor",command=scissor)
scissorbtn.grid(row=4,column=1,padx=5,pady=5)

result = Label(root,text="",font="helvica 15 bold")
result.grid(row=5,column=1)
root.mainloop()
