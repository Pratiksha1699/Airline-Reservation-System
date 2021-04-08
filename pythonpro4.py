import tkinter as tk1
from tkinter import messagebox
from tkinter.ttk import *
import psycopg2

COLOR='magenta'

def clear1():
    ent1.delete(0,'end')
    ent2.delete(0,'end')
    ent3.delete(0,'end')
    ent4.delete(0,'end')
    ent5.delete(0,'end')
    ent6.delete(0,'end')
    ent7.delete(0,'end')
    spin1.delete(0,'end')
    spin2.delete(0,'end')
    spin3.delete(0,'end')
def cont():
    print(num.get())
    date4=spin1.get()+'/'+spin2.get()+'/'+spin3.get()
    con4=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur4=con4.cursor()
    cur41=con4.cursor()
    cur4.execute("select * from user1")
    list4=cur4.fetchall()
    for j in list4:
            if(j[0]==ent6.get()):
                user=j[0]
                passwd4=j[1]
                v2=1
                break;
            else:
                v2=0
    if(v2==1):
        #print("!")
        messagebox.showwarning("INVALID",'Username Alredy Exists!')
    elif(ent1.get()=='' or ent2.get()=='' or ent3.get()=='' or ent4.get()=='' or ent5.get()=='' or ent6.get()=='' or ent7.get()==''):
        messagebox.showwarning("INVALID",'Enter all fields!')
    else:
        
        cur41.execute("insert into UserDetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(num.get(),ent1.get(),ent2.get(),date4,ent3.get(),ent4.get(),ent5.get(),ent6.get(),ent7.get()))
        con4.commit()
        cur41.execute("insert into user1 values(%s,%s)",(ent6.get(),ent7.get()))
        con4.commit()
        
        messagebox.showinfo(" ","Successful SIGNUP Login Again!")
   
                
#main window
root=tk1.Tk()
root.geometry("700x700+300+10")
root.title("Fill details!")
root.configure(bg='dark violet')
img1=tk1.PhotoImage(file="img\\pics\\Pic12.png")
img2=tk1.PhotoImage(file="img\\close7.png")
img3=tk1.PhotoImage(file="img\\lbl4.png")
img4=tk1.PhotoImage(file="img\\rb1.2.png")
backg=tk1.Label(root,image=img1).pack()

num=tk1.StringVar()

l1=tk1.Label(root,text="----PLEASE PROVIDE PASSENGER DETAILS----",font='Arial 10 bold',bg='medium blue',fg='white')
l1.place(x=50,y=20,width=400,height=40)
lbl1=tk1.Label(root,text="Title",compound='center',fg='black',font='Arial 16 bold',image=img3,bg='#000150')
lbl1.place(x=30,y=90,width=210,height=40)
lbl2=tk1.Label(root,text="First Name",compound='center',fg='black',font='Arial 16 bold',image=img3,bg='#000150')
lbl2.place(x=30,y=150,width=210,height=40)
lbl3=tk1.Label(root,text="Last Name",compound='center',fg='black',font='Arial 16 bold',image=img3,bg='#000150')
lbl3.place(x=30,y=210,width=210,height=40)
lbl4=tk1.Label(root,text="Date Of Birth",compound='center',fg='black',font='Arial 16 bold',image=img3,bg='#000150')
lbl4.place(x=30,y=270,width=210,height=40)
lbl5=tk1.Label(root,text="Address",compound='center',fg='black',font='Arial 16 bold',image=img3,bg='#000150')
lbl5.place(x=30,y=330,width=210,height=40)
lbl6=tk1.Label(root,text="Contact no",compound='center',fg='black',font='Arial 16 bold',image=img3,bg='#000150')
lbl6.place(x=30,y=390,width=210,height=40)
lbl7=tk1.Label(root,text="Email ID",compound='center',fg='black',font='Arial 16 bold',image=img3,bg='#000150')
lbl7.place(x=30,y=450,width=210,height=40)
lbl8=tk1.Label(root,text="Username",compound='center',fg='black',font='Arial 16 bold',image=img3,bg='#000150')
lbl8.place(x=30,y=510,width=210,height=40)
lbl9=tk1.Label(root,text="Password",compound='center',fg='black',font='Arial 16 bold',image=img3,bg='#000150')
lbl9.place(x=30,y=570,width=210,height=40)

title=Combobox(root,width=5,height=40,textvariable=num)
title['values']=('Mr.','Ms')
title.place(x=260,y=90)
title.current(0)

spin1=tk1.Spinbox(root,from_=1,to=30,font='Arial 13 bold',bg='yellow')
spin1.place(x=260,y=270,width=80,height=36)
spin2=tk1.Spinbox(root,from_=1,to=12,font='Arial 13 bold',bg='yellow')
spin2.place(x=350,y=270,width=80,height=36)
spin3=tk1.Spinbox(root,from_=1990,to=2015,font='Arial 13 bold',bg='yellow')
spin3.place(x=440,y=270,width=80,height=36)

ent1=tk1.Entry(root,bg='white',font="Arial 13",relief="solid",bd=0,textvariable='fname')
ent1.place(x=260,y=150,width=200,height=36)
ent1.config(highlightbackground='magenta2',highlightthickness=4)
ent2=tk1.Entry(root,bg='white',font="Arial 13",relief="solid",bd=0,textvariable='lname')
ent2.place(x=260,y=210,width=200,height=36)
ent2.config(highlightbackground='magenta2',highlightthickness=4)
ent3=tk1.Entry(root,bg='white',font="Arial 13",relief="solid",bd=0,textvariable='Address')
ent3.place(x=260,y=330,width=300,height=36)
ent3.config(highlightbackground='magenta2',highlightthickness=4)
ent4=tk1.Entry(root,bg='white',font="Arial 13",relief="solid",bd=0,textvariable='Contact')
ent4.place(x=260,y=390,width=300,height=36)
ent4.config(highlightbackground='magenta2',highlightthickness=4)
ent5=tk1.Entry(root,bg='white',font="Arial 13",relief="solid",bd=0,textvariable='Email')
ent5.place(x=260,y=450,width=300,height=36)
ent5.config(highlightbackground='magenta2',highlightthickness=4)
ent6=tk1.Entry(root,bg='white',font="Arial 13",relief="solid",bd=0,textvariable='Username')
ent6.place(x=260,y=510,width=300,height=36)
ent6.config(highlightbackground='magenta2',highlightthickness=4)
ent7=tk1.Entry(root,bg='white',font="Arial 13",relief="solid",bd=0,textvariable='Password')
ent7.place(x=260,y=570,width=300,height=36)
ent7.config(highlightbackground='magenta2',highlightthickness=4)

clear=tk1.Button(root,image=img4,bg='#000165',relief='raised',bd=0,activebackground='#000165',text='CLEAR',font='Arial 13 bold',compound='center',command=clear1)
clear.place(x=200,y=630,width=110,height=36)
cont=tk1.Button(root,image=img4,bg='#000165',relief='solid',bd=0,activebackground='#000170',text='CONTINUE',font='Arial 13 bold',compound='center',command=cont)
cont.place(x=400,y=630,width=110,height=36)

close1=tk1.Button(image=img2,relief="solid",bd=0,bg='Dark Violet',command=root.destroy)
close1.place(x=650,y=20,width=30,height=30)
root.overrideredirect(True)
root.mainloop()

