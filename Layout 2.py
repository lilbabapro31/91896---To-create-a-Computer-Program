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

root.configure(bg='#E2A1FF')

#Placement of return button
Return = Button(root, text = "RETURN", command="???")
Return.place(x=350,y=425)
Return.config(font = ("Times New Roman", 14, "bold"),width = 14, fg= "#454545", bg= "#C88AE5")

#Placement of hire button
Hire = Button(root, text = "HIRE", command="???")
Hire.place(x=140,y=425)
Hire.config(font = ("Times New Roman", 14, "bold"),width = 14,  fg= "#454545", bg= "#C88AE5")

#Placement of quit button
Quit = Button(root, text = "QUIT", command=quit)
Quit.place(x=280,y=485)
Quit.config(font = ("Times New Roman", 14, "bold"),width = 8,  fg= "#454545", bg= "#C88AE5")

result_text = tk. StringVar()

#Placement of first name and entry field
first_name = tk.Label(root, text="First Name:")
first_name.place(x=280,y=110)
entry_first_name = tk.Entry(root)
entry_first_name.place(x=235,y=140)
first_name.config(font = ("Times New Roman", 14), fg= "#454545", bg='#E2A1FF')
entry_first_name.config(font = ("Times New Roman", 14))

#Placement of last name and entry field
last_name = tk.Label(root, text="Last Name:")
last_name.place(x=280,y=170)
entry_last_name = tk.Entry(root)
entry_last_name.place(x=235,y=200)
last_name.config(font = ("Times New Roman", 14), fg= "#454545", bg='#E2A1FF')
entry_last_name.config(font = ("Times New Roman", 14))

#Placement of receipt number and entry field
receipt = tk.Label(root, text="Receipt #:")
receipt.place(x=290,y=230)
entry_receipt = tk.Entry(root)
entry_receipt.place(x=235,y=260)
receipt.config(font = ("Times New Roman", 14), fg= "#454545", bg='#E2A1FF')
entry_receipt.config(font = ("Times New Roman", 14))

#Placement of items and combobox
items = tk.Label(root, text="Items:")
items.place(x=300,y=290)
items.config(font = ("Times New Roman", 14), fg= "#454545", bg='#E2A1FF')
items_box = ttk.Combobox(root, values=["Balloons","Party Hat","Confetti","Party popper","Plates","Forks","Cups"], width=10)
items_box.place(x= 270, y= 320)
items_box.config(font = ("Times New Roman", 14))

#Placement of quantity and entry field
quantity = tk.Label(root, text="Quantity:")
quantity.place(x=290,y=350)
entry_quantity = tk.Entry(root)
entry_quantity.place(x=280,y=380)
quantity.config(font = ("Times New Roman", 14), fg= "#454545", bg='#E2A1FF')
entry_quantity.config(font = ("Times New Roman", 14), width=10)

#Placement of title
title = tk.Label(root, text = "Welcome to Julie's Party Hire store!")
title.place(x=130,y=35)
title.config(font = ("Times New Roman", 19, "bold"), fg= "#454545", bg='#E2A1FF')

root.iconbitmap(r"icon.ico")
         
root.geometry('660x540') 
root.mainloop()
