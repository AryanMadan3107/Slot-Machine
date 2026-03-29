from tkinter import *
import random
from tkinter import messagebox

def rules():
    insertmoney=startingmoney.get()
    startingmoneybutton.config(state="disabled")
    messagebox.showinfo("Rules","You are going to be gambling with €" + insertmoney + "\n After confirming starting money there is no way back \n 2 same numbers = money left * 1.5 \n 3 same numbers = money left * 3")

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

balance=Label(frame,text="Balance: €",font=("Arial",10),bg="#E1B30C",fg="white")
balance.grid(row=1,column=0)

slotframe=Frame(root,bg="#E1B30C")
slotframe.grid(row=4,column=0,pady=100)

slot1=Label(slotframe,text="7",font=("Arial",60),bg="#E6D38E",fg="white")
slot1.grid(row=0,column=0)

slot2=Label(slotframe,text="7",font=("Arial",60),bg="#E6D38E",fg="white")
slot2.grid(row=0,column=1)

slot3=Label(slotframe,text="7",font=("Arial",60),bg="#E6D38E",fg="white")
slot3.grid(row=0,column=2)

mainloop()


#balance fix