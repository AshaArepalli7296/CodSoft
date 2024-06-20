def generate_password():
    length = int(length_var.get())
    complexity = complexity_var.get()

    if complexity == "Easy":
        characters = string.ascii_letters + string.digits
    elif complexity == "Moderate":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "Hard":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        password_label.config(text="Invalid complexity level.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="" + password)

import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import random
import string

head=tk.Tk()
head.title("Password Generator")
head.configure(bg='lightpink')
head.geometry('1000x800')

Label(head,text='PASSWORD GENERATING',font=("Arial bold",25)).grid(row=1,column=22,padx=50,pady=20)

Label(head,text=' Select Complexity    ',height=2,font=('Arial bold',17)).grid(row=2,column=17,padx=50,pady=20)

complexity_var = tk.StringVar(head)
complexity_var.set("Easy")

Radiobutton(head, text="Easy       ", value="Easy",font=("Arial bold",13),height=2).grid(row=3, column=17, padx=50, pady=20)
Radiobutton(head, text="Moderate",value="Moderatre",font=("Arial bold",13),height=2).grid(row=4, column=17, padx=50, pady=20)
Radiobutton(head, text=" Hard      ",value="Hard",font=("Arial bold",13),height=2).grid(row=5, column=17, padx=50, pady=20)
Label(head,text='    Select Length       ',height=2,font=('Arial bold',17)).grid(row=2,column=21,padx=20,pady=20)

length_var = tk.StringVar(head)
length_combobox = tk.OptionMenu(head, length_var, *range(6, 21))
length_var.set(10)
length_combobox.configure(font=["Arial bold",30],width="7",bd='7')
length_combobox.grid(row=3, column=21, padx=50, pady=20)

Button(head,text="Generate Password",font=("Arial bold",17) ,bg='lightpink',bd='10',command=generate_password).grid(row=2, column=22, padx=50, pady=20)

password_label=tk.Label(head,text="",width=25,font=('Arial',20))
password_label.grid(row=3,column=22,padx=50,pady=20)



head.mainloop()