from tkinter import *
import random
from tkinter import messagebox

def rules():
    global insertmoney
    insertmoney=startingmoney.get()
    startingmoneybutton.config(state="disabled")
    messagebox.showinfo("Rules","You are going to be gambling with €" + insertmoney + "\n After confirming starting money there is no way back \n 2 same numbers = money left * 1.5 \n 3 same numbers = money left * 3 \n 0 same numbers = money left / 2")
    balancelbl.config(text="Balance: €"+insertmoney)

def slots():
    global insertmoney
    s1=random.randint(0,9)
    s2=random.randint(0,9)
    s3=random.randint(0,9)

    slot1.config(text=str(s1))
    slot2.config(text=str(s2))
    slot3.config(text=str(s3))

    if s1==s2==s3:
        insertmoney=3*int(insertmoney)
        messagebox.showinfo("Result","You won 3x your money!")
        balancelbl.config(text="Balance: €"+str(insertmoney))
    
    elif s1==s2 or s1==s3 or s2==s3:
        insertmoney=1.5*int(insertmoney)
        messagebox.showinfo("Result","You won 1.5x your money!")
        balancelbl.config(text="Balance: €"+str(insertmoney))


    else:
        insertmoney=int(insertmoney)/2
        messagebox.showinfo("Result","You lost half your money :(")
        balancelbl.config(text="Balance: €"+str(insertmoney))

def ending():
    global insertmoney
    if int(insertmoney)<1:
        slotbutton.config(state="disabled")
        messagebox.showinfo("Lost","You lost, find money and try again :(")
    elif int(insertmoney)>1000:
        slotbutton.config(state="disabled")
        messagebox.showinfo("Win","You won, go spend your money")
    else:
        slots()


    


root = Tk()
root.config(background="#E1B30C")
root.geometry("600x800")
root.title("Slot machine")

frame=Frame(root,bg="#E1B30C")
frame.grid(row=0,column=0)

title=Label(frame,text="Lucky Slot Machine",font=("Arial",30),bg="#E1B30C",fg="white")
title.grid(row=0,column=0,padx=140,pady=30)

howmuchmoney=Label(root,text="How much money will u gamble away",font=("Arial",20),bg="#E1B30C",fg="white")
howmuchmoney.grid(row=1,column=0,padx=50,pady=40)

startingmoney=Entry(root)
startingmoney.grid(row=2,column=0)

startingmoneybutton=Button(root,text="Click to confirm",command=rules)
startingmoneybutton.grid(row=3,column=0,pady=10)

balancelbl=Label(frame,text="Balance: €",font=("Arial",30),bg="#E1B30C",fg="white")
balancelbl.grid(row=1,column=0)

slotframe=Frame(root,bg="#E1B30C")
slotframe.grid(row=4,column=0,pady=100)

slot1=Label(slotframe,text="7",font=("Arial",60),bg="#E6D38E",fg="white")
slot1.grid(row=0,column=0)

slot2=Label(slotframe,text="7",font=("Arial",60),bg="#E6D38E",fg="white")
slot2.grid(row=0,column=1)

slot3=Label(slotframe,text="7",font=("Arial",60),bg="#E6D38E",fg="white")
slot3.grid(row=0,column=2)

slotbutton=Button(root,text="Spin",font=("Arial",20),command=ending)
slotbutton.grid(row=5,column=0)

mainloop()


#balance fix