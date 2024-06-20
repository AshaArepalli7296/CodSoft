
def click(sym):
    new=v.get()
    v.delete(0,tkinter.END)
    v.insert(0,new+sym) 

def clear():
    v.delete(0,tkinter.END)

def add():
    click('+')

def subtract():
    click('-')

def multiply():
    click('*')

def divide():
    click('/')

def power():
    click('**')

def cal():
   try:
         res=eval(v.get())
         v.delete(0,tkinter.END)
         v.insert(0,res) 
   except:
          v.delete(0,tkinter.END)
          v.insert(0,"Error") 
  
       
import tkinter
from tkinter import *

head=tkinter.Tk()
head.title("Calculator")
head.configure(bg="papayawhip")
v=Entry(head,width=15,borderwidth=20,fg="black",font=("Arial",30))
v.grid(padx=20, pady=30,columnspan=20,row=0,column=0)

        
button1=Button(head,text="+",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=add)
button2=Button(head,text="-",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=subtract)
button3=Button(head,text="*",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=multiply)
button4=Button(head,text="/",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=divide)
button5=Button(head,text="=",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=cal)
button6=Button(head,text="0",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('0'))
button7=Button(head,text="1",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('1'))
button8=Button(head,text="2",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('2'))
button9=Button(head,text="3",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('3'))
button10=Button(head,text="4",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('4'))
button11=Button(head,text="5",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('5'))
button12=Button(head,text="6",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('6'))
button13=Button(head,text="7",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('7'))
button14=Button(head,text="8",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('8'))
button15=Button(head,text="9",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=lambda:click('9'))
button16=Button(head,text="Clear",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=clear)
button17=Button(head,text="**",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=power)
button18=Button(head,text="Exit",font=("Arial bold",12),bg="papayawhip",padx=40,pady=20,bd='3',command=head.quit)

button1.grid(row=3,column=0,padx=17,pady=10)
button2.grid(row=3,column=1,padx=17)
button3.grid(row=3,column=2,padx=17)
button4.grid(row=4,column=0,pady=10)
button5.grid(row=4,column=1)
button6.grid(row=4,column=2)
button7.grid(row=5,column=0,pady=10)
button8.grid(row=5,column=1)
button9.grid(row=5,column=2)
button10.grid(row=6,column=0,pady=10)
button11.grid(row=6,column=1)
button12.grid(row=6,column=2)
button13.grid(row=7,column=0,pady=10)
button14.grid(row=7,column=1)
button15.grid(row=7,column=2)
button16.grid(row=8,column=0,pady=10)
button17.grid(row=8,column=1)
button18.grid(row=8,column=2)
head.mainloop()

