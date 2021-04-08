from tkinter.ttk import *
import tkinter as tk5
import os
import psycopg2
import time
from tkinter import messagebox

root5=tk5.Tk()
root5.geometry("800x700+10+20")

num51=tk5.StringVar()
num52=tk5.StringVar()
num53=tk5.StringVar()
rb5=tk5.IntVar()

#images used
img5=tk5.PhotoImage(file="img\\pics\\img5.1.png")
img51=tk5.PhotoImage(file="img\\Aviation1.2.png")
img52=tk5.PhotoImage(file="img\\Aviation2.1.png")
img53=tk5.PhotoImage(file="img\\btn7-0.png")
img54=tk5.PhotoImage(file="img\\btn7-1.png")
img55=tk5.PhotoImage(file="img\\Aviation1.8.png")
img56=tk5.PhotoImage(file="img\\Aviation2.8.png")
img57=tk5.PhotoImage(file="img\\lbl1.png")
imgclose5=tk5.PhotoImage(file="img\\close7.png")
    
#methods used
def change51():
    Searchbtn1.config(image=img53)
def rbsel():
    if(rb5.get()==1):
        print(rb5.get())
        lbl53.lower(w5)
        spin4.lower(w5)
        spin5.lower(w5)
        spin6.lower(w5)
        
    elif(rb5.get()==2):
        print(rb5.get())
        lbl53.lift(w5)
        spin4.lift(w5)
        spin5.lift(w5)
        spin6.lift(w5)
        
        
def searchbtn1def():
    Searchbtn1.config(image=img54)
    Searchbtn1.after(400,change51)
    img5=tk5.PhotoImage(file="img\\pics\\img5.1.png")
    listFly=[]
    listDeparttime=[]
    listArrivaltime=[]
    listseat=[]
    listcharges=[]
    listid=[]
    v5=0
    if(rb5.get()==0):
        messagebox.showinfo("SELECT ONE OPTION",'select ONE WAY or ROUND TRIP!')
    elif(rb5.get()==1):
        if(num51.get()==num52.get()):
            messagebox.showwarning("INVALID ENTRIES",'Source and Destination cannot be same!')
        elif(usrtxt5.get()==''):
            messagebox.showwarning('FIll ALL ENTRIES','Please enter username')
        else:
            con50=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
            cur50=con50.cursor()
            cur50.execute("select * from user1")
            row0=cur50.fetchall()
            for j in row0:
                if(j[0]==usrtxt5.get()):
                    user5=j[0]
                    pass5=j[1]
                    v50=1
                    break;
                else:
                    v50=0
            if(v50==0):
                messagebox.showwarning("Invalid User",'Enter valid username!')
            elif(v50==1):
                #valid user, checking flight for one way trip
                con51=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
                cur51=con51.cursor()
                cur51.execute("select * from FlightDetails")
                row51=cur51.fetchall()
                for i in row51:
                    if(i[1]==num51.get() and i[2]==num52.get() and i[5]==num53.get() and i[7]!=0):
                        Total=int(spin7.get())+int(spin8.get())
                        #print(Total)
                        #print(i)
                        if(int(i[7])>=Total):
                            listFly.append(i[0])
                            listDeparttime.append(i[3])
                            listArrivaltime.append(i[4])
                            listcharges.append(i[6])
                            listseat.append(i[7])
                            listid.append(i[9])
                            print("Flight:",listFly)
                            print("src:",num51.get())
                            print('Des:',num52.get())
                            print('Class:',num53.get())
                            print('depart time:',listDeparttime)
                            print('Arrive time:',listArrivaltime)
                            print('Seat:',listseat)
                            print('Charges:',listcharges)
                            print("listid's:",listid)
                            v5=1
                            #break;
                    else:
                        print("No match!")
                if(v5==1):
                    msg1=messagebox.askquestion(" ",'Flight FOUND! Do you want to enter further details?')
                    if(msg1=='yes'):
                        print("message is yes!")
                        date50=spin1.get()+'/'+spin2.get()+'/'+spin3.get()
                        adult=spin7.get()
                        children=spin8.get()
                        cur52=con51.cursor()
                        cur52.execute('delete from passengerdetails1 where Username=%s',(usrtxt5.get(),))
                        con51.commit()
                        cur52.execute('insert into passengerdetails1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(usrtxt5.get(),num51.get(),num52.get(),date50,'',adult,children,num53.get(),'ONE WAY'))
                        #check before insertion if booking already exists!
                        cur52.execute('delete from passengerdetails2 where username2=%s',(usrtxt5.get(),))
                        con51.commit()
                        print("Deleted previous transactions")
                        cur52.execute('insert into passengerdetails2 values(%s,%s,%s,%s)',(usrtxt5.get(),num51.get(),num52.get(),listid))
                        con51.commit()
                        con51.close()
                        os.system('pythonproCDetails.py')
                    
                    else:
                        print("message is no!")
                elif(v5==0):
                    messagebox.showinfo(" ","Flight not found Try Again Later!")
    elif(rb5.get()==2):
        if(num51.get()==num52.get()):
            messagebox.showwarning("INVALID ENTRIES",'Source and Destination cannot be same!')
        elif(usrtxt5.get()==''):
            messagebox.showwarning('FIll ALL ENTRIES','Please enter username')
        else:
            v51=0
            con52=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
            cur5=con52.cursor()
            cur5.execute("select * from user1")
            row1=cur5.fetchall()
            for j in row1:
                if(j[0]==usrtxt5.get()):
                    user5=j[0]
                    pass5=j[1]
                    v51=1
                    break;
                else:
                    v51=0
            if(v51==0):
                messagebox.showwarning("Invalid User",'Enter valid username!')
            elif(v51==1):
                #valid user, checking flight for round trip
                vr5=0
                f2=''
                f1=''
                con52=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
                cur5=con52.cursor()
                cur5.execute("select * from FlightDetails")
                row53=cur5.fetchall()
                print(row53)
                for i in row53:
                    #if(i[0]==num51.get() and i[1]==num52.get() and i[5]==num53.get() and i[7]!=0)
                    if(i[1]==num51.get() and i[2]==num52.get() and i[5]==num53.get()):
                        Total1=int(spin7.get())+int(spin8.get())
                        #print(Total)
                        #print(i)
                        print("inside if")
                        if(int(i[7])>=Total1):
                            f1=i[0]
                            listFly.append(i[0])
                            listDeparttime.append(i[3])
                            listArrivaltime.append(i[4])
                            listcharges.append(i[6])
                            listseat.append(i[7])
                            listid.append(i[9])
                            vr5=1
                            print('f1',f1)
                for i in row53:
                    
                    if(i[2]==num51.get() and i[1]==num52.get() and i[5]==num53.get() and i[7]!=0):
                        Total2=int(spin7.get())+int(spin8.get())
                        #print(Total)
                        #print(i)
                        f2=i[0]
                        if(int(i[7])>=Total2 and f2==f1):
                            #f2=i[0]
                            listFly.append(i[0])
                            listDeparttime.append(i[3])
                            listArrivaltime.append(i[4])
                            listcharges.append(i[6])
                            listseat.append(i[7])
                            listid.append(i[9])
                            print('f2',f2)
                            vr5=2
                            print('vr5',vr5)
                            break;
                if(vr5==2):
                    print("Flight found!")
                    msg2=messagebox.askquestion(" ",'Flight FOUND! Do you want to enter further details?')
                    if(msg2=='yes'):
                        print("message is yes!")
                        date51=spin1.get()+'/'+spin2.get()+'/'+spin3.get()
                        date52=spin4.get()+'/'+spin5.get()+'/'+spin6.get()
                        adult2=spin7.get()
                        children2=spin8.get()
                        cur5=con52.cursor()
                        cur5.execute('delete from passengerdetails1 where Username=%s',(usrtxt5.get(),))
                        con52.commit()
                        cur5.execute('insert into passengerdetails1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(usrtxt5.get(),num51.get(),num52.get(),date51,date52,adult2,children2,num53.get(),'ROUND TRIP'))
                        #check before insertion if booking already exists!
                        print("Deleting prevoius transactions!")
                        cur5.execute('delete from passengerdetails2 where username2=%s',(usrtxt5.get(),))
                        con52.commit()
                        cur5.execute('insert into passengerdetails2 values(%s,%s,%s,%s,%s,%s)',(usrtxt5.get(),num51.get(),num52.get(),listid,date51,date52))
                        con52.commit()
                        con52.close()
                        os.system('pythonproCDetails.py')
                    else:
                        print("no match!")
                else:
                    messagebox.showinfo(" ",'Flight not found Try Again Later!')
                    
                    
w5=tk5.Label(root5,image=img5).pack()

b1=tk5.Radiobutton(root5,text="ONE WAY",image=img51,value=1,font='Arial 9 bold',var=rb5,indicatoron=0,selectimage=img55,compound="top",command=rbsel)
b1.place(x=200,y=30)
b2=tk5.Radiobutton(root5,text="ROUND TRIP",image=img52,value=2,font='Arial 9 bold',var=rb5,indicatoron=0,selectimage=img56,compound="top",command=rbsel)
b2.place(x=380,y=30)

lbl50=tk5.Label(root5,text="Username:",image=img57,bg='cyan',font='Arial 10 bold',compound='center')
lbl50.place(x=100,y=180,height=40,width=100)
lbl51=tk5.Label(root5,text="Leaving From:",image=img57,bg='cyan',font='Arial 10 bold',compound='center')
lbl51.place(x=100,y=250,height=40,width=100)
lbl52=tk5.Label(root5,text="Depart Date:",image=img57,bg='cyan',font='Arial 10 bold',compound='center')
lbl52.place(x=100,y=320,height=40,width=100)
lbl53=tk5.Label(root5,text="Return Date:",image=img57,bg='cyan',font='Arial 10 bold',compound='center')
lbl53.place(x=100,y=400,height=40,width=100)
lbl54=tk5.Label(root5,text="Adult:",image=img57,bg='cyan',font='Arial 10 bold',compound='center')
lbl54.place(x=100,y=476,height=40,width=100)
lbl55=tk5.Label(root5,text="Going To:",bg='cyan',font='Arial 10 bold',compound='center')
lbl55.place(x=420,y=250,height=40,width=100)
lbl56=tk5.Label(root5,text="Children:",bg='cyan',font='Arial 10 bold',compound='center')
lbl56.place(x=420,y=476,height=40,width=100)
lbl57=tk5.Label(root5,text="Class:",bg='cyan',font='Arial 10 bold',compound='center')
lbl57.place(x=100,y=550,height=40,width=100)

usrtxt5=tk5.Entry(root5,bg='white',font="Arial 13 bold",relief="solid",bd=0)
usrtxt5.config(highlightbackground='white',highlightthickness=4,highlightcolor='purple')
usrtxt5.place(x=210,y=180,width=200,height=40)


c51=Combobox(root5,width=5,height=40,textvariable=num51,font='Arial 13 bold')
c51['values']=('Mumbai','Kolkata','Ahmedabad','Aurangabad','Bhuvaneshwar','Coimbatore','Chennai','Dehradun','Gaya','Indore','Imphal','Jaipur','Jodhpur','Kanniyakumari','Kochi','Kota','Lucknow','Madurai','Mysore','Nashik','Patna','Rajkot','Shimla','Thiruvananthapuram','Vadodra','Goa','Delhi','Hyderabad')
c51.place(x=210,y=250,height=40,width=200)
c51.current(0)
#print(num51.get())

spin1=tk5.Spinbox(root5,from_=1,to=31,font='Arial 13 bold',bg='green yellow')
spin1.place(x=230,y=320,width=80,height=36)
spin2=tk5.Spinbox(root5,from_=1,to=12,font='Arial 13 bold',bg='green yellow')
spin2.place(x=320,y=320,width=80,height=36)
spin3=tk5.Spinbox(root5,from_=2019,to=2030,font='Arial 13 bold',bg='green yellow')
spin3.place(x=410,y=320,width=80,height=36)

spin4=tk5.Spinbox(root5,from_=1,to=31,font='Arial 13 bold',bg='green yellow')
spin4.place(x=230,y=400,width=80,height=36)
spin5=tk5.Spinbox(root5,from_=1,to=12,font='Arial 13 bold',bg='green yellow')
spin5.place(x=320,y=400,width=80,height=36)
spin6=tk5.Spinbox(root5,from_=2019,to=2030,font='Arial 13 bold',bg='green yellow')
spin6.place(x=410,y=400,width=80,height=36)

spin7=tk5.Spinbox(root5,from_=1,to=10,font='Arial 13 bold',bg='yellow')
spin7.place(x=230,y=476,width=40,height=36)
spin8=tk5.Spinbox(root5,from_=0,to=5,font='Arial 13 bold',bg='yellow')
spin8.place(x=530,y=476,width=40,height=36)

Searchbtn1=tk5.Button(root5,text="Search Flight",compound='center',font='Arial 13 bold',bd=0,image=img53,bg='dodger blue',command=searchbtn1def)
Searchbtn1.place(x=300,y=630,width=160,height=60)

c52=Combobox(root5,width=5,height=40,textvariable=num52,font='Arial 13 bold')
c52['values']=('Mumbai','Kolkata','Ahmedabad','Aurangabad','Bhuvaneshwar','Coimbatore','Chennai','Dehradun','Gaya','Indore','Imphal','Jaipur','Jodhpur','Kanniyakumari','Kochi','Kota','Lucknow','Madurai','Mysore','Nashik','Patna','Rajkot','Shimla','Thiruvananthapuram','Vadodra','Goa','Delhi','Hyderabad')
c52.place(x=530,y=250,height=40,width=200)
c52.current(0)

c53=Combobox(root5,width=5,height=40,textvariable=num53,font='Arial 13 bold')
c53['values']=('Economy','Premium Economy','Business','First Class')
c53.place(x=210,y=550,height=40,width=200)
c53.current(0)

close=tk5.Button(root5,image=imgclose5,bg='DeepSkyBlue2',bd=0,highlightthickness=0,activebackground='white',command=root5.destroy)
close.place(x=750,y=10,width=30,height=30)

root5.overrideredirect(True)
root5.mainloop()
