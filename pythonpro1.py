import os
import psycopg2
#import runpy
#import sys
import tkinter as tk
from tkinter import messagebox
COLOR='magenta'
#main window
root=tk.Tk()
root.geometry("550x600+300+100")
#images used
img=tk.PhotoImage(file="img\\pics\\Picture1.png")
img1=tk.PhotoImage(file="img\\Gionee-M6-Mirror-Stock-Walls-2.png")
img2=tk.PhotoImage(file="img\\admin3.png")
img3=tk.PhotoImage(file="img\\user1.png")
img4=tk.PhotoImage(file="img\\user3.png")
img5=tk.PhotoImage(file="img\\admin4.png")
img6=tk.PhotoImage(file="img\\apply1.png")
img9=tk.PhotoImage(file="img\\note1.png")
img10=tk.PhotoImage(file="img\\check1.png")
img11=tk.PhotoImage(file="img\\close4.png")
img12=tk.PhotoImage(file="img\\close5.png")

v=tk.IntVar()
rb=tk.IntVar()
#method used
def quit1():
    root.destroy()
def reset():
    usrtxt.delete(0,'end')
    pwd.delete(0,'end')
def showpwd():
    if(v.get()==1):
        print("chkbox clicked!!")
        pwd.config(show="")
    elif(v.get()==0):
        print("chbox unclicked!!")
        pwd.config(show="*")

def login1():
    #root.destroy()
    #os.system('radiobutton.py')
    #exec(open("radiobutton.py").read())
    if(rb.get()==0):
        print("select a user!")
        messagebox.showinfo("SELECT ONE","Select a user!!")
    elif(rb.get()==1):
        print("ADMIN")
        passwd=[]
        admin=[]
        v=1
        conn=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
        cur=conn.cursor()
        cur.execute("select * from admin")
        rows=cur.fetchall()
        for i in rows:
            if(i[0]==usrtxt.get()):
                admin=i[0]
                passwd=i[1]
                v=1
                break;
            else:
                v=0
        if(v==0):
            print("Enter correct username!")
            messagebox.showwarning("INVALID",'Enter correct username!')
            
        else:
            print("username is correct")
            if(passwd==pwd.get()):
                #print("user:",admin)
                #print("pass:",passwd)
                os.system('pythonpro3.py')
                
            else:
                messagebox.showwarning("INVALID","Enter correct password!")
        
        
    elif(rb.get()==2):
        print("USER")
        passwd2=[]
        user=[]
        v2=1
        conn=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
        cur=conn.cursor()
        cur.execute("select * from user1")
        rowu=cur.fetchall()
        for j in rowu:
            if(j[0]==usrtxt.get()):
                user=j[0]
                passwd2=j[1]
                v2=1
                break;
            else:
                v2=0
        if(v2==0):
            print("Enter correct username!")
            messagebox.showwarning("INVALID",'Enter correct username!')
            
        else:
            print("username is correct")
            if(passwd2==pwd.get()):
                #print("user:",user)
                #print("pass:",passwd2)
                os.system('pythonpro5.1.py')
                
            else:
                messagebox.showwarning("INVALID","Enter correct password!")
        
def signup1():
    print("Signing UP!!")
    a=0
    if(rb.get()==0):
        messagebox.showinfo('SELECT ONE',"select a user!!")
    elif(rb.get()==1):
        messagebox.showinfo(' ',"CANNOT SIGNUP AS ADMIN")
    elif(rb.get()==2):
        con2=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
        cur1=con2.cursor()
        cur1.execute("select * from user1")
        row1=cur1.fetchall()
        #for k in row1:
            #if(k[0]==usrtxt.get()):
                #messagebox.showinfo(" ","Username already exists!Try another")
                #a=1
                #break;
            #else:
                #a=0
        if(a==1):
            messagebox.showinfo(" ","Username already exists!Try another")
        elif(a==0):
            #cur1.execute("insert into user1 values(%s,%s)",(usrtxt.get(),pwd.get()))
            #con2.commit()
            #print("successful signup!")
            #messagebox.showinfo('Signup','Fill Details')
            os.system('pythonpro4.py')
            

w1=tk.Label(root,image=img).pack()
b1=tk.Radiobutton(root,text="ADMIN",image=img2,value=1,var=rb,indicatoron=0,selectimage=img5)
b1.place(x=100,y=50)
b2=tk.Radiobutton(root,text="USER",image=img3,value=2,var=rb,indicatoron=0,selectimage=img4)
b2.place(x=300,y=50)
username=tk.Label(root,text="USERNAME:",font="Arial 14",bg='purple',fg='white')
username.place(x=100,y=300)
usrtxt=tk.Entry(root,bg='white',font="Arial 13",relief="solid",bd=0)
usrtxt.config(highlightbackground=COLOR,highlightthickness=4)
usrtxt.place(x=100,y=340,width=200,height=45)
password=tk.Label(root,text="PASSWORD:",font="Arial 14",bg='purple',fg='white')
password.place(x=100,y=395)
pwd=tk.Entry(root,bg='white',font="Arial 13",relief="solid",bd=0,show='*',textvariable='passwd')
pwd.place(x=100,y=435,width=200,height=45)
pwd.config(highlightbackground=COLOR,highlightthickness=4)
login=tk.Button(root,text="LOGIN",image=img6,font="Arial 12",compound='center',bd=0,bg='MediumOrchid1',relief='solid',highlightthickness=0,activebackground='MediumOrchid1',command=login1)
login.place(x=400,y=440,width=80,height=45)
signup=tk.Button(root,text="SIGNUP",image=img6,font="Arial 12",compound='center',bg='MediumOrchid1',relief='solid',bd=0,highlightthickness=0,activebackground='MediumOrchid1',command=signup1)
signup.place(x=420,y=490,width=80,height=45)
reset=tk.Button(root,text="RESET",image=img6,font="Arial 12",compound='center',bg='MediumOrchid1',relief='solid',bd=0,highlightthickness=0,activebackground='MediumOrchid1',command=reset)
reset.place(x=440,y=540,width=80,height=45)
check=tk.Checkbutton(root,image=img9,selectimage=img10,var=v,bg='MediumOrchid1',selectcolor='MediumOrchid1',activebackground='MediumOrchid1',highlightthickness=0,indicatoron=0,bd=0,command=showpwd)
check.place(x=300,y=435,width=50,height=45)
close=tk.Button(root,image=img11,bg='MediumOrchid1',bd=0,highlightthickness=0,activebackground='MediumOrchid2',command=quit1)
close.place(x=510,y=10,width=30,height=30)
#to make undecorated frame
root.overrideredirect(True)
#root.resizable(width=100,height=100)
root.mainloop()
