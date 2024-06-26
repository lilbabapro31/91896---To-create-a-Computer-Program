#Author: Harry Hsieh
#Date: 13/6/24
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

#Placement of return button
Return = Button(root, text = "RETURN", command="???")
Return.place(x=365,y=320)
Return.config(font = ("Arial", 14),width = 14)

#Placement of hire button
Hire = Button(root, text = "HIRE", command="???")
Hire.place(x=125,y=320)
Hire.config(font = ("Arial", 14),width = 14)

#Placement of quit button
Quit = Button(root, text = "QUIT", command=quit)
Quit.place(x=515,y=385)
Quit.config(font = ("Arial", 14),width = 8)

result_text = tk. StringVar()

#Placement of first name and entry field
first_name = tk.Label(root, text="First Name:")
first_name.place(x=145,y=90)
entry_first_name = tk.Entry(root)
entry_first_name.place(x=265,y=95)
first_name.config(font = ("Arial", 14))
entry_first_name.config(font = ("Arial", 14))

#Placement of last name and entry field
last_name = tk.Label(root, text="Last Name:")
last_name.place(x=145,y=150)
entry_last_name = tk.Entry(root)
entry_last_name.place(x=265,y=155)
last_name.config(font = ("Arial", 14))
entry_last_name.config(font = ("Arial", 14))

#Placement of receipt number and entry field
receipt = tk.Label(root, text="Receipt #:")
receipt.place(x=145,y=205)
entry_receipt = tk.Entry(root)
entry_receipt.place(x=265,y=210)
receipt.config(font = ("Arial", 14))
entry_receipt.config(font = ("Arial", 14))

#Placement of item combobox
items_box = ttk.Combobox(root, values=["Ballons","Party Hat","Confetti","Party popper","Plates","Forks","Cups"], width=15)
items_box.place(x =125, y= 260)
items_box.config(font = ("Arial", 14))

#Placement of amount and entry field
amount = tk.Label(root, text="Amount:")
amount.place(x=335,y=260)
entry_amount = tk.Entry(root)
entry_amount.place(x=415,y=260)
amount.config(font = ("Arial", 14))
entry_amount.config(font = ("Arial", 14), width=10)

#Placement of title
title = tk.Label(root, text = "Welcome to Julie's Party Hire store!")
title.place(x=135,y=30)
title.config(font = ("Arial", 17))

root.geometry('650x450') 
root.mainloop()
