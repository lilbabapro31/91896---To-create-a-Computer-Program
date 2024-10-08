#Author: Harry Hsieh
#Date: 5/8/24
#Purpose: To create a GUI for Julie's part hire store

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import random

history_data = []
party_items = ["Balloons","Party Hat","Confetti","Party popper","Plates","Forks","Cups"]
def validate_first_name(first_name):
        return first_name.isalpha()

def validate_last_name(last_name):
        return last_name.isalpha()

def validate_Receipt(Receipt):
    if Receipt.isdigit():
        Receipt = int(Receipt)

def validate_item_selection(value):
        return value in party_items

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
def setup_bg(canvas):
        #Placement of logo/image
        from tkinter import PhotoImage
        global bg
        bg = PhotoImage(file="julie party logo.png")
        bg = bg.subsample(2)
        canvas.create_image(0, 0, anchor=NW, image=bg)
        global Background
        Background = PhotoImage(file="FINAL GUI INTERFACE BG.png")
        canvas2.create_image(0, 0, anchor=NW, image=Background)

def hire():
    # Get the input data
    first_name_data = entry_first_name.get()
    last_name_data = entry_last_name.get()
    item_data = items_box.get()
    item_count_data = entry_quantity.get()

    # Validate the input data
    if not first_name_data or not last_name_data or not item_data or not item_count_data:
        messagebox.showerror("Error", "All fields must be filled out")
        return

    if not validate_item_selection(item_data):
        messagebox.showerror("Error", "Invalid item selected")
        return

    if not validate_Amount(item_count_data):
        messagebox.showerror("Error", "Item count must be between 1 and 500")
        return

    # Generate a new receipt number for each hire
    receipt = random.randint(1, 100)

    # Add the input data to the history list
    entry_data = (first_name_data, last_name_data, receipt, item_data, item_count_data)
    history_data.append(entry_data)

    # Clear the input fields
    entry_first_name.delete(0, END)
    entry_last_name.delete(0, END)
    items_box.set('')
    entry_quantity.delete(0, END)

    messagebox.showinfo("Hire", f"Submission successful! Your receipt number is {receipt}.")


#GUI Title
root = tk.Tk()
root.title("Julie's Party Hire store")

root.configure(bg='lightblue')
canvas2 = Canvas(root, width=670, height=450, bg='lightblue', bd=0, highlightthickness=0)
canvas2.place(x=0, y=0)
canvas = Canvas(root, width=165, height=135, bg='lightblue', bd=0, highlightthickness=0)
canvas.place(x=10, y=0)
setup_bg(canvas)
#Placement of history button
History = Button(root, text = "HISTORY", command=history)
History.place(x=375,y=320)
History.config(font = ("Comic Sans MS", 14, "bold"),width = 14, fg= "#454545", bg= "#ABD3E3")

#Placement of hire button
Hire = Button(root, text = "HIRE", command=hire)
Hire.place(x=135,y=320)
Hire.config(font = ("Comic Sans MS", 14, "bold"),width = 14,  fg= "#454545", bg= "#ABD3E3")


#Placement of quit button
Quit = Button(root, text = "QUIT", command=quit)
Quit.place(x=515,y=385)
Quit.config(font = ("Comic Sans MS", 14, "bold"),width = 8,  fg= "#454545", bg= "#92C0D2")


result_text = tk. StringVar()

#Placement of first name and entry field
first_name = tk.Label(root, text="First Name:")
first_name.place(x=145,y=130)
entry_first_name = tk.Entry(root, validate="key")
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
items_box = ttk.Combobox(root,value=party_items, width=10)
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
title.place(x=175,y=45)
title.config(font = ("Comic Sans MS", 19, "bold"), fg= "#454545", bg='lightblue')


root.iconbitmap(r"icon.ico")

root.geometry('670x450') 
root.mainloop()
