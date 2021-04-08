import tkinter as tk2
import time
from tkinter import messagebox
from tkinter import *
import psycopg2
root5=tk2.Tk()
root5.geometry('600x700+300+20')
#images used
imgbg=tk2.PhotoImage(file="img\\asus_zenfone_max_plus_droidviews_01.png")
imgclose=tk2.PhotoImage(file="img\\close7.png")
imgb1=tk2.PhotoImage(file="img\\btn10_1.png")
imgb11=tk2.PhotoImage(file="img\\btn10_2.png")
imgbadd=tk2.PhotoImage(file="img\\search.png")
imglbl=tk2.PhotoImage(file="img\\lbl6.png")

#can=tk2.Canvas(root5,bg='yellow')
#can.place(x=100,y=250,width=400,height=400)
#can.lower(root5)

def change1():
     B1.config(image=imgb1)
    
def view():
    B1.config(image=imgb11)
    B1.after(300,change1)
    print("Viewing Admins")
    can=tk2.Canvas(root5,bg='misty rose',scrollregion=(0,0,700,700))
    can.place(x=100,y=280,width=400,height=400)

    conn=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur1=conn.cursor()
    cur1.execute("select * from admin")
    rowno=cur1.rowcount
    rows=cur1.fetchall()
    j,k,count=0,0,0
    for i in rows:
        admin=i[0]
        lblad=tk2.Label(can,bg='misty rose',image=imglbl,text=admin,compound='center',font='Arial 15 bold',fg='Black')
        lblad.place(x=j+5,y=k+10,width=120,height=60)
        j=j+130
        count=count+1
        if(count==3):
            k=k+100
            j=0
            count=0
   
def add():
     print('ADDING ADMIN')
     def adminadd():
          name1=Nametxt.get()
          passwd1=Passtxt.get()
          print(name1)
          print(passwd1)
          a=0
          con3=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
          cur2=con3.cursor()
          cur2.execute("select * from admin")
          row1=cur2.fetchall()
          R1=cur2.rowcount
          print(R1)
          for k in row1:
                 if(k[0]==Nametxt.get()):
                     #messagebox.showinfo(" ","Username already exists!Try another")
                     a=1
                     break;
                 elif(Nametxt.get()=='' or Passtxt.get()==''):
                      a=2
                      break;
                 elif(R1==12):
                      a=3
                      
                     
          if(a==1):
                 messagebox.showinfo(" ","Admin already exists!Try another")
          elif(a==2):
               messagebox.showinfo("NULL VALUE","Fill all Entries!")
          elif(a==3):
               messagebox.showwarning("Space Full!",'Cannot insert more than 12 admins')
          elif(a==0):
               cur2.execute("insert into admin values(%s,%s)",(Nametxt.get(),Passtxt.get()))
               con3.commit()
               print("successful!")
               messagebox.showinfo('ADMIN','added new admin Sucessfully!Login again')
            

          
     Name=tk2.Label(root5,bg='cyan',text='Enter ADMIN name:',font='Arial 10 bold')
     Name.place(x=35,y=180,height=40,width=120)
     Nametxt=tk2.Entry(root5,bg='white',font="Arial 13",relief="solid",bd=0)
     Nametxt.place(x=170,y=180,height=40,width=130)
     Nametxt.config(highlightbackground='deep sky blue',highlightthickness=4)
     Name=tk2.Label(root5,bg='cyan',text='Enter password:',font='Arial 10 bold')
     Name.place(x=310,y=180,height=40,width=120)
     Passtxt=tk2.Entry(root5,bg='white',font="Arial 13",relief="solid",bd=0)
     Passtxt.place(x=440,y=180,height=40,width=130)
     Passtxt.config(highlightbackground='deep sky blue',highlightthickness=4)
     addadmin=tk2.Button(root5,image=imgbadd,text="ADD ADMIN",compound="center",bd=0,bg='deep sky blue',font="Arial 13 bold",activebackground='#1a75c2',highlightthickness=0,command=adminadd)
     addadmin.place(x=240,y=230,width=120,height=40)
     
lblbg=tk2.Label(root5,image=imgbg).pack()

B1=tk2.Button(root5,image=imgb1,text="VIEW ADMIN",compound="center",bd=0,bg='#1a75c2',font="Arial 13 bold",activebackground='#1a75c2',highlightthickness=0,command=view)
B1.place(x=100,y=100,width=170,height=60)

B2=tk2.Button(root5,image=imgb1,text="ADD ADMIN",compound="center",bd=0,bg='#1a75c2',font="Arial 13 bold",activebackground='#1a75c2',highlightthickness=0,command=add)
B2.place(x=330,y=100,width=170,height=60)

close=tk2.Button(root5,image=imgclose,bg='deep sky blue',bd=0,highlightthickness=0,activebackground='white',command=root5.destroy)
close.place(x=550,y=10,width=30,height=30)

root5.overrideredirect(True)
root5.mainloop()
