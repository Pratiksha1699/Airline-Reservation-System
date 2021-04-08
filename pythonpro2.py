import tkinter as tk2
import os
import sys
from tkinter import *
from tkinter import messagebox
import psycopg2
root2=tk2.Tk()
root2.geometry("700x550+30+30")
img=tk2.PhotoImage(file="img\\img72.png")
img1=tk2.PhotoImage(file="img\\comment0-2.png")

w22=tk2.Label(root2,image=img).pack()

def feedback():
    can1=tk2.Canvas(root2,bg='white')
    can1.place(x=30,y=100,height=400,width=600)
    Sc=tk2.Scrollbar(can1,orient=VERTICAL,command=can1.yview)
    Sc.pack(fill=Y,side=RIGHT)
    
    can1.configure(yscrollcommand=Sc.set)
    con2=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur2=con2.cursor()
    cur2.execute("select * from feedback")
    row2=cur2.fetchall()
    n=20
    for i in row2:
        textlbl=i[0]
        t=tk2.Label(can1,text=textlbl,font='Times 12 italic',bg='RosyBrown1')
        t.place(x=20,y=n,width=550,height=50)
        can1.create_window(300,n,window=t,width=550,height=50)
        n=n+60

    can1.config(scrollregion=(0,0,600,n))
        
    


btn=tk2.Button(root2,text='SHOW\nFEEDBACK',image=img1,compound='center',font='Arial 12 bold',relief='solid',bd=0,command=feedback)
btn.place(x=30,y=30,width=120,height=60)

root2.configure(bg='white')
root2.mainloop()
