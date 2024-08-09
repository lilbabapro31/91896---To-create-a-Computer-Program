#Author: Harry Hsieh
#Date: 5/8/24
#Purpose: To create a GUI for Julie's part hire store

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def validate_first_name(first_name):
        return first_name.isalpha()

def validate_last_name(last_name):
        return last_name.isalpha()

def validate_Receipt(Receipt):
    if Receipt.isdigit():
        Receipt = int(Receipt)

def validate_Item(Item):
        return Item.isalpha()

def validate_Amount(Amount):
    if Amount.isdigit():
        Amount = int(Amount)
        if 1 <= Amount <= 500:
            return True
    return False

def quit():
        root.destroy()

def display_contents():

    first_name = entry_first_name.get()
    Receipt = entry_Receipt.get()

    if not validate_first_name(first_name):
        messagebox.showerror("Invalid Input", "First Name must be only alphabets.")
        return

    last_name = entry_last_name.get()
    Receipt = entry_Receipt.get()

    if not validate_last_name(last_name):
        messagebox.showerror("Invalid Input", "Last Name must be only alphabets.")
        return

    if not validate_Amount(Amount):
                messagebox.showerror("Invalid Input", "Amount must be a number between 1 and 500.")
                return
#End message
    result_text.set("First Name: {first_name}, Receipt#: {Receipt#}")
#GUI Title
root = tk.Tk()
root.title("Julie's Party Hire store")

root.configure(bg='lightblue')

#Placement of return button
Return = Button(root, text = "RETURN", command="???")
Return.place(x=375,y=320)
Return.config(font = ("Comic Sans MS", 14, "bold"),width = 14, fg= "#454545", bg= "#ABD3E3")

#Placement of hire button
Hire = Button(root, text = "HIRE", command="???")
Hire.place(x=125,y=320)
Hire.config(font = ("Comic Sans MS", 14, "bold"),width = 14,  fg= "#454545", bg= "#ABD3E3")

#Placement of quit button
Quit = Button(root, text = "QUIT", command=quit)
Quit.place(x=515,y=385)
Quit.config(font = ("Comic Sans MS", 14, "bold"),width = 8,  fg= "#454545", bg= "#92C0D2")

result_text = tk. StringVar()

#Placement of first name and entry field
first_name = tk.Label(root, text="First Name:")
first_name.place(x=145,y=130)
entry_first_name = tk.Entry(root)
entry_first_name.place(x=265,y=135)
first_name.config(font = ("Comic Sans MS", 14), fg= "#454545", bg='lightblue')
entry_first_name.config(font = ("Comic Sans MS", 14))

#Placement of last name and entry field
last_name = tk.Label(root, text="Last Name:")
last_name.place(x=150,y=200)
entry_last_name = tk.Entry(root)
entry_last_name.place(x=265,y=205)
last_name.config(font = ("Comic Sans MS", 14), fg= "#454545", bg='lightblue')
entry_last_name.config(font = ("Comic Sans MS", 14))

#Placement of items and combobox
items = tk.Label(root, text="Items:")
items.place(x=115,y=260)
items.config(font = ("Comic Sans MS", 14), fg= "#454545", bg='lightblue')
items_box = ttk.Combobox(root, values=["Balloons","Party Hat","Confetti","Party popper","Plates","Forks","Cups"], width=10)
items_box.place(x =180, y= 260)
items_box.config(font = ("Comic Sans MS", 14))

#Placement of quantity and entry field
quantity = tk.Label(root, text="Quantity:")
quantity.place(x=335,y=260)
entry_quantity = Spinbox(root, from_=1, to=500)
entry_quantity.place(x=425,y=260)
quantity.config(font = ("Comic Sans MS", 14), fg= "#454545", bg='lightblue')
entry_quantity.config(font = ("Comic Sans MS", 14), width=10)

#Placement of title
title = tk.Label(root, text = "Welcome to Julie's Party Hire store!")
title.place(x=115,y=45)
title.config(font = ("Comic Sans MS", 19, "bold"), fg= "#454545", bg='lightblue')

root.iconbitmap(r"icon.ico")

root.geometry('670x450') 
root.mainloop()
