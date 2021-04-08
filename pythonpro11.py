from tkinter import *
from tkinter import messagebox
import psycopg2
import tkinter as tk

root10=tk.Tk()
root10.geometry('900x600+30+40')
img1=PhotoImage(file="img\\image7.png")
img2=PhotoImage(file="img\\impmsg3.png")
img3=PhotoImage(file="img\\close7.png")
w1=Label(root10,image=img1)
w1.pack()

def ContactDetails():
    print("Contact Details")

    con42=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur42=con42.cursor()
    cur42.execute("select * from UserDetails")
    list1=cur42.fetchall()
    R=len(list1)
    C=len(list1[0])
    print("rows:",R)
    print("column:",C)
    c1=tk.Canvas(root10,bg="NavyBlue")
    c1.place(x=60,y=250,width=820,height=300)
    #c1.pack(side=LEFT,expand=True,fill=BOTH)
    Sc=Scrollbar(c1,orient=VERTICAL)
    Sc.pack(side=RIGHT,fill=Y)
    lbl=Label(root10,text='Mr/Ms |FirstName |LastName |Date of Birth|Address |Contact No|Email |Username |Password',font='Arial 12 bold',bg='white').place(x=60,y=200,width=790,height=40)
    k=n=0
    lbl=[]
    for i in range(R):
        lbl.append(i)
        lbl[i]=tk.Entry(c1)
        lbl[i].place(x=0,y=n,width=790,height=30)
        lbl[i].pack()
        for j in range(C):
            s11=list1[i][j]
            E=tk.Entry(lbl[i],fg='blue',font=('Arial',10,'bold'),relief='solid',bd=0)
            E.place(x=k,y=0,height=30,width=80)
            E.config(highlightthickness=2)
            E.insert(END,list1[i][j])
            k=k+80
        
        c1.create_window(400,n,window=lbl[i],width=790,height=30)
        n=n+40
        k=0
    c1.config(width=500,height=400,scrollregion=(0,0,790,n),yscrollcommand=Sc.set)
    Sc.config(command=c1.yview)

def BookDetails():
    con42=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur42=con42.cursor()
    cur42.execute("select * from PassengerDetails1")
    list1=cur42.fetchall()
    R=len(list1)
    C=len(list1[0])
    print("rows:",R)
    print("column:",C)
    c1=tk.Canvas(root10,bg="blue")
    c1.place(x=60,y=250,width=820,height=300)
    #c1.pack(side=LEFT,expand=True,fill=BOTH)
    Sc=Scrollbar(c1,orient=VERTICAL)
    Sc.pack(side=RIGHT,fill=Y)
    lbl=Label(root10,text='Username |Source |Destination |Depart Date|Return Date |Adults|Children |Class |Type of trip',font='Arial 12 bold',bg='white').place(x=60,y=200,width=790,height=40)
    k=n=0
    lbl=[]
    for i in range(R):
        lbl.append(i)
        lbl[i]=tk.Entry(c1)
        lbl[i].place(x=0,y=n,width=720,height=30)
        lbl[i].pack()
        for j in range(C):
            s11=list1[i][j]
            E=tk.Entry(lbl[i],fg='blue',font=('Arial',10,'bold'),relief='solid',bd=0)
            E.place(x=k,y=0,height=30,width=80)
            E.config(highlightthickness=2)
            E.insert(END,list1[i][j])
            k=k+80
        
        c1.create_window(400,n,window=lbl[i],width=790,height=30)
        n=n+40
        k=0
    c1.config(width=500,height=400,scrollregion=(0,0,720,n),yscrollcommand=Sc.set)
    Sc.config(command=c1.yview)

    

Btn1=Button(root10,image=img2,relief='solid',bd=0,activebackground='turquoise1',bg='dodger blue',compound='center',text="View User's Contact Details",font='Arial 15 bold',command=ContactDetails)
Btn1.place(x=100,y=50,height=45,width=550)

Btn2=Button(root10,image=img2,relief='solid',bd=0,activebackground='turquoise1',bg='dodger blue',compound='center',text="View User's Booking Details",font='Arial 15 bold',command=BookDetails)
Btn2.place(x=100,y=120,height=45,width=550)



close10=Button(root10,image=img3,command=root10.destroy,relief='solid',bd=0,activebackground='blue',bg='blue')
close10.place(x=850,y=20,height=30,width=30)

root10.overrideredirect(True)
root10.mainloop()
