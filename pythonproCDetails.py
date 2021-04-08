import tkinter as tk8
from tkinter import *
import psycopg2
from tkinter import messagebox
import os
import sys

root8=tk8.Tk()
img8=tk8.PhotoImage(file="img\\img8_2.png")
imgclose8=tk8.PhotoImage(file="img\\close7.png")
img81=tk8.PhotoImage(file="img\\lbl7_3.png")
img82=tk8.PhotoImage(file="img\\note1.png")
img83=tk8.PhotoImage(file="img\\check1.png")
img84=tk8.PhotoImage(file="img\\lbl7_3.png")
root8.geometry('1000x700+10+10')
w8=tk8.Label(root8,image=img8).pack()
rb8=tk8.StringVar()
#var1=tk8.StringVar()
#var2=tk8.StringVar()
rb8.set(" ")
A=B=[]
var1=[]
var2=[]
v8=tk8.IntVar()
def showpwd8():
    if(v8.get()==1):
        print("chkbox clicked!!")
        pwdtxt8.config(show="")
    elif(v8.get()==0):
        print("chkbox unclicked!!")
        pwdtxt8.config(show="$")
def rbvalue():
    if(rb8.get()!=""):
        print("rb value:",rb8.get())
        c1=tk8.Canvas(root8,bg='magenta2')
        c1.place(x=550,y=60,width=400,height=300)
        c2=tk8.Canvas(root8,bg='maroon1')
        c2.place(x=550,y=370,width=400,height=300)

        sb1=tk8.Scrollbar(c1,orient=VERTICAL,bg='pink',command=c1.yview)
        sb1.pack(fill=Y,side=RIGHT)
        c1.config(scrollregion=(0,0,550,600))
        c1.configure(yscrollcommand=sb1.set)

        sb2=tk8.Scrollbar(c2,orient=VERTICAL,bg='pink',command=c2.yview)
        sb2.pack(fill=Y,side=RIGHT)
        c2.config(scrollregion=(0,0,550,600))
        c2.configure(yscrollcommand=sb2.set)

        
        
        l1=tk8.Label(c1,text="ADULTS",bg='yellow',font='Arial 12 bold')
        l1.pack()
        c1.create_window(100,20,window=l1,width=100,height=30)

        l2=tk8.Label(c2,text="CHILDREN",bg='yellow',font='Arial 12 bold')
        l2.pack()
        c2.create_window(100,20,window=l2,width=100,height=30)

        con81=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
        cur81=con81.cursor()
        cur81.execute("select * from PassengerDetails1")
        row81=cur81.fetchall()
        for k in row81:
            if(k[0]==usrtxt8.get()):
                adult=int(k[5])
                children=int(k[6])
                print(type(adult))
                print(adult)
                print(children)
                break;
        m=20
        n=60
        p=m+180
        for j in range(0,adult):
            Albl=tk8.Label(c1,text="Enter Name:",bg='White')
            Albl.place(x=m,y=n,width=80,height=40)
            c1.create_window(80,n,window=Albl,width=80,height=40)
            var1.append(StringVar())
            Ent=tk8.Entry(c1,font="Arial 13 bold",relief="solid",bd=0,textvariable=var1[j])
            Ent.place(x=p,y=n,width=150,height=40)
            Ent.config(highlightbackground='yellow',highlightthickness=4,highlightcolor='Orange')
            c1.create_window(p,n,window=Ent,width=150,height=40)
            n=n+50

        m=20
        n=60
        p=m+180
        for i in range(0,children):
            Clbl=tk8.Label(c2,text="Enter Name:",bg='White')
            Clbl.place(x=m,y=n,width=80,height=40)
            c2.create_window(80,n,window=Clbl,width=80,height=40)
            var2.append(StringVar())
            Entc=tk8.Entry(c2,font="Arial 13 bold",relief="solid",bd=0,textvariable=var2[i])
            Entc.place(x=p,y=n,width=150,height=40)
            Entc.config(highlightbackground='yellow',highlightthickness=4,highlightcolor='Orange')
            c2.create_window(p,n,window=Entc,width=150,height=40)
            n=n+50

def Submit1():
    print("Rb val:",rb8.get())
    A=[]
    C=[]
    print("Var1 len:",len(var1))
    print("var2 len:",len(var2))
    for i in range(0,len(var1)):
        print("EntriesA:",var1[i].get())
        A.append(var1[i].get())
    for j in range(0,len(var2)):
        print("ENtriesC:",var2[j].get())
        C.append(var2[j].get())

    #con82=psycopg2.connect()
    con82=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur82=con82.cursor()
    cur82.execute('delete from passengerdetails3 where Username=%s',(usrtxt8.get(),))
    #cur82.execute("delete from PassengerDetails3 where Username=%s",(usrtxt8.get(),))
    
    cur82.execute("insert into PassengerDetails3 values(%s,%s,%s,%s)",(usrtxt8.get(),rb8.get(),A,C))
    con82.commit()
    messagebox.showinfo("SUBMIT",'Details Submitted Sucessfully!Proceed to Payment Details')
    os.system('pythonpro9.py')
    
        
    
        
            
       
        

        

def ShowFlight():
    
    passwd8=[]
    user=[]
    v81=1
    listID=[]
    listID1=[]
    con8=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur8=con8.cursor()
    cur8.execute("select * from user1")
    row8=cur8.fetchall()
    for j in row8:
        if(j[0]==usrtxt8.get()):
            user=j[0]
            passwd8=j[1]
            v2=1
            break;
        else:
            v2=0
    if(v2==0):
        print("Enter correct username!")
        messagebox.showwarning("INVALID",'Enter correct username!')
            
    else:
        print("username is correct")
        if(passwd8==pwdtxt8.get()):
            print("user:",user)
            print("pass:",passwd8)
            #show flights
            username=usrtxt8.get()
            print(username)
            v82=0
            cur8.execute("select * from passengerdetails2")
            row81=cur8.fetchall()
            #print(row81)
            for i in row81:
                if(username==i[0]):
                    #print("Username found!")
                    listID=i[3]
                    v82=1
                    break;
                else:
                    v82=0
            if v82==1:
                print("Username found!")
                listID1=listID.split(',')
                print(listID1)
                str1=str(listID)
                #print(listID1[0][0])
                #print(listID1)
                #print('str:',str1)
                str2=str1.replace('{','')
                str3=str2.replace('}','')
                print("String3:",str3)
                L=str3.split(',')
                print("L:",L)
                cur81=con8.cursor()
                cur81.execute("select * from FlightDetails")
                row8=cur81.fetchall()
                j=0
                k=30
                m=300
                Length=len(L)
                for i in row8:
                    if(i[9]==L[j]):
                        lbl=tk8.Label(root8,text='Please select a Flight of your choice',font='Arial 10 italic',bg='yellow')
                        lbl.place(x=k,y=230)
                        lbl11=tk8.Label(root8,text='Flight',font='Arial 14 italic',bg='yellow')
                        lbl11.place(x=k,y=260)
                        lbl12=tk8.Label(root8,text='Arrival Time',font='Arial 14 italic',bg='yellow')
                        lbl12.place(x=180,y=260)
                        lbl13=tk8.Label(root8,text='Depart Time',font='Arial 14 italic',bg='gold')
                        lbl13.place(x=290,y=260)
                        lbl14=tk8.Label(root8,text='Charges',font='Arial 14 italic',bg='yellow')
                        lbl14.place(x=400,y=260)

                        Submit=tk8.Button(root8,text='SUBMIT',command=Submit1)
                        Submit.place(x=200,y=600,width=150,height=40)
                        radio1=tk8.Radiobutton(root8,image=img81,variable=rb8,value=i[0],text=i[0],compound='center',command=rbvalue,bg='Light Sky Blue',font='Arial 12 italic bold')
                        radio1.place(x=k,y=m)
                        k=k+150
                        lbl1=tk8.Label(root8,image=img84,text=i[3],compound='center',bg='yellow',font='Arial 12 italic bold')
                        lbl1.place(x=k,y=m)
                        k=k+110
                        lbl2=tk8.Label(root8,image=img84,text=i[4],compound='center',bg='yellow2',font='Arial 12 italic bold')
                        lbl2.place(x=k,y=m)
                        k=k+110
                        lbl3=tk8.Label(root8,image=img84,text=i[6],compound='center',bg='yellow',font='Arial 12 italic bold')
                        lbl3.place(x=k,y=m)
                        m=m+50
                        k=30
                        j=j+1
                        if(j==Length):
                            break;
                    
                    
                
                    
        else:
            messagebox.showwarning("INVALID","Enter correct password!")
            
lbl81=tk8.Label(root8,bg='gold',text='Passenger Details',font='Arial 15 bold')
lbl81.place(x=40,y=30,height=40,width=300)

lbl82=tk8.Label(root8,bg='yellow',image=img81,relief='solid',compound='center',text='Username:',font='Arial 12 bold',bd=0)
lbl82.place(x=30,y=80,width=150,height=45)
lbl83=tk8.Label(root8,bg='yellow',image=img81,relief='solid',compound='center',text='Password:',font='Arial 12 bold',bd=0)
lbl83.place(x=30,y=130,width=150,height=45)
usrtxt8=tk8.Entry(root8,bg='white',font="Arial 13",relief="solid",bd=0)
usrtxt8.config(highlightbackground='yellow',highlightthickness=4,highlightcolor='gold')
usrtxt8.place(x=200,y=80,width=200,height=45)
pwdtxt8=tk8.Entry(root8,bg='white',font="Arial 13 bold",relief="solid",bd=0)
pwdtxt8.config(highlightbackground='yellow',highlightthickness=4,highlightcolor='gold',show='$')
pwdtxt8.place(x=200,y=130,width=200,height=45)

check8=tk8.Checkbutton(root8,image=img82,selectimage=img83,var=v8,bg='light sky blue',selectcolor='light sky blue',activebackground='light sky blue',highlightthickness=0,indicatoron=0,bd=0,command=showpwd8)
check8.place(x=400,y=130,width=50,height=45)

Seeflight=tk8.Button(root8,text='Show Flights',command=ShowFlight)
Seeflight.place(x=200,y=180,width=150,height=40)

closeimg8=tk8.Button(root8,image=imgclose8,command=root8.destroy,relief='solid',bg='white',bd=0)
closeimg8.place(x=950,y=20,width=30,height=30)
root8.overrideredirect(True)
root8.mainloop()
