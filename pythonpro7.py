import tkinter as tk3
from tkinter import *
from tkinter.ttk import *
import psycopg2
import os
from tkinter import messagebox

root3=tk3.Tk()
root3.geometry('1000x700+10+20')
imgbg7=tk3.PhotoImage(file="img\\bg4.png")#make bg4
imgclose=tk3.PhotoImage(file="img\\close10.png")#make close10
img71=tk3.PhotoImage(file="img\\btn6-5.png")
img72=tk3.PhotoImage(file="img\\lbl7_2.png")

num0=StringVar()
num1=StringVar()
num2=StringVar()
num3=StringVar()
num4=StringVar()
num5=StringVar()

def addF():
    if(ent71.get()=='' or ent72.get()=='' or ent73.get()==''):
        messagebox.showwarning("Warning",'Enter all information!')
    else:
        m=0
        s1=int(ent72.get())
        date1=spin1.get()+'/'+spin2.get()+'/'+spin3.get()
        con71=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
        cur7=con71.cursor()
        cur7.execute("select * from FlightDetails")
        rows=cur7.fetchall()
        for i in rows:
            if(i[9]==ent73.get()):
                
                m=1
                break;
            else:
                m=0
        
        if(m==1):
            messagebox.showinfo("Cannot ADD",'Flight already exists!')
        elif(m==0):
            
            print(date1)
            print(type(date1))
            cur7.execute("insert into FlightDetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(num0.get(),num1.get(),num2.get(),num3.get(),num4.get(),num5.get(),ent71.get(),ent72.get(),date1,ent73.get()))
            con71.commit()
            print("Sucessfully added Flight")
            messagebox.showinfo("ADDED",'Sucessfully added Flight details!')
        con71.close()

def DeleteF():
    date2=spin1.get()+'/'+spin2.get()+'/'+spin3.get()
    del1=ent71.get()
    del2=ent72.get()
    del3=ent73.get()
    con72=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur72=con72.cursor()
    cur72.execute("select * from FlightDetails")
    rows=cur72.fetchall()
    for i in rows:
        if(i[0]==num0.get() and i[1]==num1.get() and i[2]==num2.get() and i[3]==num3.get() and i[4]==num4.get() and i[5]==num5.get() and i[6]==ent71.get() and i[7]==ent72.get() and i[8]==date2 and i[9]==ent73.get()):
            m=1
            cur72.execute("Delete from FlightDetails where Fname=%s and Source1=%s and Destination=%s and Departure=%s and Arrival=%s and Class1=%s and Charges=%s and Seats=%s and Date11=%s and id1=%s",(num0.get(),num1.get(),num2.get(),num3.get(),num4.get(),num5.get(),del1,del2,date2,del3))
            con72.commit()
            con72.close()
            break;
        else:
            m=0
    if(m==0):
        messagebox.showinfo("Cannot DELETE","Flight Doesn't exists at all!")
    elif(m==1):
        messagebox.showinfo("DELETED","Flight Deleted Sucessfully!")
    
def UpdateF():
    if(ent71.get()=='' or ent72.get()=='' or ent73.get()==''):
        messagebox.showwarning("Warning",'Enter all information!')
    else:
        
        date7=spin1.get()+'/'+spin2.get()+'/'+spin3.get()
        del1=ent71.get()
        del2=ent72.get()
        del3=ent73.get()
        con75=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
        cur75=con75.cursor()
        cur75.execute("select * from FlightDetails")
        rows=cur75.fetchall()
        for i in rows:
            if(i[9]==ent73.get()):
                m=1
                cur75.execute("Update FlightDetails set Fname=%s,Source1=%s,Destination=%s,Departure=%s,Arrival=%s,Class1=%s,Charges=%s,Seats=%s,Date11=%s where id1=%s",(num0.get(),num1.get(),num2.get(),num3.get(),num4.get(),num5.get(),del1,del2,date7,del3))
                con75.commit()
                con75.close()
                break;
            else:
                m=0
        if(m==0):
            messagebox.showinfo("Cannot UPDATE","Flight Doesn't exists at all!")
        elif(m==1):
            messagebox.showinfo("UPDATED","Flight Modified Sucessfully!")
        

def reset_Scr(event):
    c1.configure(scrollregion=(0,0,740,500))

def ViewF():
    date1=spin1.get()+'/'+spin2.get()+'/'+spin3.get()
    con71=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur7=con71.cursor()
    cur7.execute("select * from FlightDetails")
    list1=cur7.fetchall()
    R=len(list1)
    C=len(list1[0])
    #print(C)
    root4=tk3.Tk()
    root4.geometry('650x500+30+30')
    root4.rowconfigure(0,weight=1)
    root4.columnconfigure(0,weight=1)
    c1=tk3.Canvas(root4,bg='NavyBlue')
    c1.place(x=0,y=30,width=740,height=400)
    c1.pack(side=LEFT,expand=True,fill=BOTH)
    Sc=tk3.Scrollbar(root4,orient=VERTICAL)
    Sc.pack(side=RIGHT,fill=Y)
    #c1.bind("<Configure>",reset_Scr(root4.Sc))
    #c1.create_polygon(10,10,300,50,10,100)
    k=n=0
    lbl=[]
    for i in range(R):
        lbl.append(i)
        lbl[i]=tk3.Entry(c1)
        lbl[i].place(x=0,y=n,width=790,height=30)
        lbl[i].pack()
        for j in range(C):
            s11=list1[i][j]
            E=tk3.Entry(lbl[i],fg='blue',font=('Arial',10,'bold'))
            E.place(x=k,y=0,height=30,width=80)
            E.insert(END,list1[i][j])
            k=k+80
        
        c1.create_window(400,n,window=lbl[i],width=790,height=30)
        n=n+30
        k=0
    c1.config(width=500,height=400,scrollregion=(0,0,740,n),yscrollcommand=Sc.set)
    Sc.config(command=c1.yview)
    root4.mainloop()

def searchID():
    con73=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur73=con73.cursor()
    cur73.execute("select * from FlightDetails")
    row=cur73.fetchall()
    w=0
    for i in row:
        if(i[9]==ent73.get()):
            w=1
            c0.set(i[0])
            c1.set(i[1])
            c2.set(i[2])
            c3.set(i[3])
            c4.set(i[4])
            c5.set(i[5])
            date4=i[8]
            d1=date4.split('/')
            s1=d1[0]
            s2=d1[1]
            s3=d1[2]
            print('s1,s2,s3',s1)
            print(s2)
            print(s3)
            spin1.delete(0,END)
            spin2.delete(0,END)
            spin3.delete(0,END)
            ent71.delete(0,END)
            ent72.delete(0,END)
            ent71.insert(END,i[6])
            ent72.insert(END,i[7])
            spin1.insert(END,s1)
            spin2.insert(END,s2)
            spin3.insert(END,s3)
            break;
        else:
            w=0
    if(w==0):
        messagebox.showinfo('INVALID ID','ID Not Found!')
    con73.commit()
    con73.close()

            
        


lbg=tk3.Label(root3,image=imgbg7).pack()

lbl0=tk3.Label(root3,text="FLIGHT DETAILS",font='Arial 28 bold',bg='Yellow')
lbl0.place(x=20,y=30,width=500,height=50)
lbl1=tk3.Label(root3,text="FLIGHT NAME",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl1.place(x=20,y=110,width=200,height=50)
lbl2=tk3.Label(root3,text="SOURCE",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl2.place(x=20,y=180,width=200,height=50)
lbl3=tk3.Label(root3,text="DEPARTURE",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl3.place(x=20,y=250,width=200,height=50)
lbl4=tk3.Label(root3,text="FLIGHT CLASS",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl4.place(x=20,y=320,width=200,height=50)
lbl5=tk3.Label(root3,text="FLIGHT CHARGES",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl5.place(x=20,y=390,width=200,height=50)
lbl6=tk3.Label(root3,text="SEATS",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl6.place(x=20,y=460,width=200,height=50)
lbl7=tk3.Label(root3,text="DESTINATION",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl7.place(x=460,y=180,width=200,height=50)
lbl8=tk3.Label(root3,text="ARRIVAL",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl8.place(x=460,y=250,width=200,height=50)
lbl9=tk3.Label(root3,text="DATE",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl9.place(x=20,y=530,width=200,height=50)
lbl10=tk3.Label(root3,text="FLIGHT ID",font='Arial 15 bold',image=img72,compound='center',bg='white')
lbl10.place(x=460,y=110,width=200,height=50)

c0=Combobox(root3,width=5,height=40,textvariable=num0,font='Arial 13 bold')
c0['values']=('Air India','Jet Airways','IndiGo','SpiceJet','GoAir','AirAsia India','Vistara','Air India Express')
c0.place(x=230,y=110,height=45,width=200)
c0.current(0)
print(num0.get())


c1=Combobox(root3,width=5,height=40,textvariable=num1,font='Arial 13 bold')
c1['values']=('Mumbai','Kolkata','Ahmedabad','Aurangabad','Bhuvaneshwar','Coimbatore','Chennai','Dehradun','Gaya','Indore','Imphal','Jaipur','Jodhpur','Kanniyakumari','Kochi','Kota','Lucknow','Madurai','Mysore','Nashik','Patna','Rajkot','Shimla','Thiruvananthapuram','Vadodra','Goa','Delhi','Hyderabad')
c1.place(x=230,y=180,height=45,width=200)
c1.current(0)
print(num1.get())

c2=Combobox(root3,width=5,height=40,textvariable=num2,font='Arial 13 bold')
c2['values']=('Mumbai','Kolkata','Ahmedabad','Aurangabad','Bhuvaneshwar','Coimbatore','Chennai','Dehradun','Gaya','Indore','Imphal','Jaipur','Jodhpur','Kanniyakumari','Kochi','Kota','Lucknow','Madurai','Mysore','Nashik','Patna','Rajkot','Shimla','Thiruvananthapuram','Vadodra','Goa','Delhi','Hyderabad')
c2.place(x=670,y=180,height=45,width=200)
c2.current(0)
print(num2.get())

c3=Combobox(root3,width=5,height=40,textvariable=num3,font='Arial 13 bold')
c3['values']=('1:00','2:00','3:00','4:00','5:00','6:00','7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','24:00')
c3.place(x=230,y=250,height=45,width=200)
c3.current(0)
print(num3.get())

c4=Combobox(root3,width=5,height=40,textvariable=num4,font='Arial 13 bold')
c4['values']=('1:00','2:00','3:00','4:00','5:00','6:00','7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','24:00')
c4.place(x=670,y=250,height=45,width=200)
c4.current(0)
print(num4.get())

c5=Combobox(root3,width=5,height=40,textvariable=num5,font='Arial 13 bold')
c5['values']=('Economy','Premium Economy','Business','First Class')
c5.place(x=230,y=320,height=45,width=200)
c5.current(0)
print(num5.get())



#ent71=tk3.Entry(root3,bg='white',font="Arial 13",relief="solid",bd=0)
#ent71.config(highlightbackground='indian red',highlightthickness=4)
#ent71.place(x=230,y=110,width=200,height=50)
#ent72=tk3.Entry(root3,bg='white',font="Arial 13",relief="solid",bd=0)
#ent72.config(highlightbackground='indian red',highlightthickness=4)
#ent72.place(x=230,y=250,width=200,height=50)
#ent73=tk3.Entry(root3,bg='white',font="Arial 13",relief="solid",bd=0)
#ent73.config(highlightbackground='indian red',highlightthickness=4)
#ent73.place(x=230,y=320,width=200,height=50)
ent71=tk3.Entry(root3,bg='white',font="Arial 13",relief="solid",bd=0)
ent71.config(highlightbackground='indian red',highlightthickness=4)
ent71.place(x=230,y=390,width=200,height=50)
ent72=tk3.Entry(root3,bg='white',font="Arial 13",relief="solid",bd=0)
ent72.config(highlightbackground='indian red',highlightthickness=4)
ent72.place(x=230,y=460,width=200,height=50)
ent73=tk3.Entry(root3,bg='white',font="Arial 13",relief="solid",bd=0)
ent73.config(highlightbackground='indian red',highlightthickness=4)
ent73.place(x=670,y=110,width=200,height=50)

search1=tk3.Button(root3,bg='white',text='SEARCH',font="Arial 13",relief='solid',bd=0,command=searchID)
search1.place(x=890,y=110,width=100,height=50)

#ent76=tk3.Entry(root3,bg='white',font="Arial 13",relief="solid",bd=0)
#ent76.config(highlightbackground='indian red',highlightthickness=4)
#ent76.place(x=670,y=180,width=200,height=50)
#ent77=tk3.Entry(root3,bg='white',font="Arial 13",relief="solid",bd=0)
#ent77.config(highlightbackground='indian red',highlightthickness=4)
#ent77.place(x=670,y=250,width=200,height=50)

spin1=tk3.Spinbox(root3,from_=1,to=31,font='Arial 13 bold',bg='yellow')
spin1.place(x=230,y=530,width=80,height=36)
spin2=tk3.Spinbox(root3,from_=1,to=12,font='Arial 13 bold',bg='yellow')
spin2.place(x=320,y=530,width=80,height=36)
spin3=tk3.Spinbox(root3,from_=2019,to=2030,font='Arial 13 bold',bg='yellow')
spin3.place(x=410,y=530,width=80,height=36)

add71=tk3.Button(root3,text="ADD FLIGHT",bg='Hot Pink',font='Arial 13 bold',relief='solid',bd=0,activebackground='blue',compound="center",image=img71,command=addF)
add71.place(x=20,y=600,width=160,height=60)
add72=tk3.Button(root3,text="DELETE",bg='Hot Pink',font='Arial 13 bold',relief='solid',bd=0,activebackground='blue',compound="center",image=img71,command=DeleteF)
add72.place(x=250,y=600,width=160,height=60)
add73=tk3.Button(root3,text="UPDATE",bg='Hot Pink',font='Arial 13 bold',relief='solid',bd=0,activebackground='blue',compound="center",image=img71,command=UpdateF)
add73.place(x=480,y=600,width=160,height=60)
add74=tk3.Button(root3,text="VIEW",bg='Hot Pink',font='Arial 13 bold',relief='solid',bd=0,activebackground='blue',compound="center",image=img71,command=ViewF)
add74.place(x=710,y=600,width=160,height=60)
#add75.place()


close7=tk3.Button(root3,image=imgclose,command=root3.destroy,relief='solid',bd=0,activebackground='turquoise1',bg='blue')
close7.place(x=950,y=20,height=30,width=30)
root3.overrideredirect(True)
root3.mainloop()
