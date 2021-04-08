import tkinter as tk
import os
import sys
from tkinter import messagebox

    
#COLOR='magenta'
#main window
root2=tk.Tk()
root2.geometry("550x600+300+100")
#images used:
img=tk.PhotoImage(file="img\\pics\\bg1.png")
img1=tk.PhotoImage(file="img\\btn2-0.png")
img2=tk.PhotoImage(file="img\\close7.png")

#method used
def Flight_Details():
    os.system('pythonpro7.py')

def Admin_Details():
    os.system('pythonpro5.py')

def Passenger_Details():
    os.system('pythonpro11.py')

def Pass_details():
    os.system('pythonpro2.py')


w2=tk.Label(root2,image=img).pack()
b1=tk.Button(image=img1,text="Flight Details",font="Arial 14 bold",compound="center",relief="solid",bd=0,bg='magenta',activebackground='Dark Violet',command=Flight_Details)
b1.place(x=80,y=105,width=190,height=190)
b2=tk.Button(image=img1,text="View\nPassenger\nDetails",font="Arial 14 bold",compound="center",relief="solid",bd=0,bg='magenta',activebackground='Dark Violet',command=Passenger_Details)
b2.place(x=280,y=105,width=190,height=190)
b3=tk.Button(image=img1,text="Passenger\nFeedback",font="Arial 14 bold",compound="center",relief="solid",bd=0,bg='magenta',activebackground='Dark Violet',command=Pass_details)
b3.place(x=80,y=305,width=190,height=190)
b4=tk.Button(image=img1,text="Admin Details",font="Arial 14 bold",compound="center",relief="solid",bd=0,bg='magenta',activebackground='Dark Violet',command=Admin_Details)
b4.place(x=280,y=305,width=190,height=190)
close1=tk.Button(image=img2,relief="solid",bd=0,bg='Dark Violet',command=root2.destroy)
close1.place(x=500,y=30,width=30,height=30)

#root2.configure(bg=COLOR)
root2.overrideredirect(True)
root2.mainloop()
