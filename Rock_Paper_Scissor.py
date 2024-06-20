def start() :
    Label(head,text='  Choose your option  ', bg="gainsboro",height=2,fg='black',font=('Arial bold',25),).grid(row=2,columnspan=10,padx=100,pady=10)
    b1=tk.Button(head,text="  Rock 🪨",bg="bisque",fg='black',bd='10',font=('Arial bold',25),command=lambda:play_game('Rock'))
    b1.grid(padx=10,pady=20,row=3,column=5)
    b2=tk.Button(head,text=" Paper 📜",bg="bisque",fg='black',bd='10',font=("Arial bold",25),command=lambda:play_game('Paper'))
    b2.grid(padx=10,pady=20,row=4,column=5)
    b3=tk.Button(head,text=" Scissor ✂",bg="bisque",bd='10',fg='black',font=('Arial bold',25),command=lambda:play_game('Scissor'))
    b3.grid(padx=10,pady=20,row=5,column=5)
user_score = 0
comp_score = 0

def clear() :
    head.destroy()

def play_game(user_choice):
    global user_score, comp_score
    choices = ['Rock', 'Paper', 'Scissor']
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        user_score+=0
        comp_score+=0
        messagebox.showinfo('',"IT IS A TIE!..........\n\nClick OK to see score")
    elif (user_choice == 'Rock' and comp_choice == 'Scissor') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
          messagebox.showinfo('',"YOU WIN!............ \n\nClick OK to see score")
          user_score += 1
    else:
       messagebox.showinfo('',"COMPUTER WINS!..........\n\nClick OK to see score") 
       comp_score += 1
      
    user_label=tk.Label(head, text="    Your Score:     ",height=2, font=('Arial bold', 20)).grid(row=3, column=13, padx=10, pady=20)
    e1=Entry(head,width=10,font=('Arial ',35))
    e1.grid(row=3,column=17,padx=10,pady=20)
    e1.insert(0,user_score)

    comp_label=tk.Label(head, text=" Computer Score:  ", height=2,font=('Arial bold', 20)).grid(row=4, column=13, padx=10, pady=20) 
    e2=Entry(head,width=10,font=('Arial ',35))
    e2.grid(row=4,column=17,padx=10,pady=20)
    e2.insert(0,comp_score)

    Button(head,text="   Exit   ",bg="aqua",bd='10',fg='black',font=('Arial bold',25),command=clear).grid(row=5,column=15,padx=10,pady=20)
    
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

head=Tk()
head.title("Game")

head.configure(bg="dimgrey")
Button(head,text='      "ROCK,PAPER,SCISSOR"---- GAME      ',bd='10',height=2,background='gainsboro',fg='black',font=("Arial bold",30)).grid(row=0,columnspan=30,padx=400,pady=10)
head.geometry('1000x1000')
Button(head,text='Tap To Start',bg="aqua",bd='10',fg='black',font=('Arial bold',25),command=start).grid(row=1,columnspan=35,padx=400,pady=10)


head.mainloop()