import tkinter as tk6
from tkinter import *
from tkinter import messagebox
import os
import psycopg2

root6=tk6.Tk()
root6.geometry('700x700+100+20')

payvar=300000.0

def Pay():
    amount=int(ent1.get())
    deduced=payvar-amount
    print("Duducted amt:",deduced)
    if deduced<0:
        messagebox.showwarning("NOT ENOUGH BALANCE","Cannnot pay due to insuficient balance!")
    else:
        msg=messagebox.showinfo("PAYMENT","PAYMENT DONE SUCCESSFULLY!")
        if msg:
            #msg1=messagebox.showinfo(" ","Do You want to Fill Feedback")
            print("payment successful!")
            os.system('FinalReceipt.py')
            
def show():
    f1=0
    conn=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur=conn.cursor()
    cur2=conn.cursor()
    cur3=conn.cursor()
    cur.execute("select * from passengerdetails1")
    cur2.execute("select * from FlightDetails")
    cur3.execute("select * from PassengerDetails3")
    row9=cur.fetchall()
    row91=cur2.fetchall()
    row92=cur3.fetchall()
    for i in row9:
        if(i[0]==ent0.get()):
            f1=1
            src=i[1]
            des=i[2]
            adult=i[5]
            child=i[6]
            class1=i[7]
            type1=i[8]
            break;
        else:
            f1=0
    if(f1==0):
        print("Invalid User!")
        messagebox.showwarning("PAYMENT","Enter correct Username!")
    elif(f1==1):
        print('Valid User')
        for i in row92:
            if(i[0]==ent0.get()):
                fname=i[1]
                break;
        for i in row91:
            if(i[0]==fname and i[1]==src and i[2]==des and i[5]==class1):
                charges=i[6]
                break;
        print(int(charges))
        amt1=int(adult)*int(charges)
        amt2=int(child)*int(charges)*0.8
        amt=0
        amt=amt1+amt2
        
        if(class1=='Economy'):
            amt=amt*0.75
        elif(class1=='Premium Economy'):
            amt=amt*0.80
        elif(class1=='Business'):
            amt=amt*1
        else:
            amt=amt*0.7

        if(type1=='ROUND TRIP'):
            amt=amt*2

        amt=amt+0.3*(int(charges))+0.05*(int(charges))
        ent1.delete(0,'end')
        ent1.insert('end',int(amt))
        ent1.config(state='disabled')
        

            


imgbg1=tk6.PhotoImage(file="img\\imgbg20.png")
imgclose=tk6.PhotoImage(file="img\\close7.png")#make close10
img71=tk6.PhotoImage(file="img\\btn9.0.png")
img61=tk6.PhotoImage(file="img\\lbl2.png")

lbg=tk6.Label(root6,image=imgbg1).pack()


lbl0=tk6.Label(root6,text="PAYMENT DETAILS",font='Arial 28 bold',bg='yellow')
lbl0.place(x=20,y=30,width=500,height=50)

lblname=tk6.Label(root6,text="USER",font='Arial 15 bold',bg='yellow')
lblname.place(x=20,y=110,width=400,height=50)
ent0=tk6.Entry(root6,bg='white',font="Arial 13",relief="solid",bd=0)
ent0.config(highlightbackground='indian red',highlightthickness=4,highlightcolor='yellow')
ent0.place(x=430,y=110,width=200,height=50)

lbl1=tk6.Label(root6,text="MAKE A PAYMENT OF RS",font='Arial 15 bold',bg='yellow')
lbl1.place(x=20,y=180,width=400,height=50)
lbl2=tk6.Label(root6,text="PAY THE GIVEN AMOUNT",font='Arial 15 bold',bg='yellow')
lbl2.place(x=20,y=260,width=400,height=50)


ent1=tk6.Entry(root6,bg='white',font="Arial 13",relief="solid",bd=0)
ent1.config(highlightbackground='indian red',highlightthickness=4,highlightcolor='yellow')
ent1.place(x=430,y=180,width=200,height=50)

#ent1.configure(state='disabled')

conn=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
cur=conn.cursor()
cur.execute("select * from passengerdetails3")
rows=cur.fetchall()

add1=tk6.Button(root6,text="MAKE PAYMENT",font='Arial 13 bold',relief='solid',bd=0,compound="center",image=img71,command=Pay)
add1.place(x=500,y=460,width=160,height=65)

show=tk6.Button(root6,text="SHOW",font='Arial 13 bold',relief='solid',bd=0,compound="center",command=show)
show.place(x=640,y=110,width=55,height=50)


close7=tk6.Button(root6,image=imgclose,command=root6.destroy,relief='solid',bd=0,activebackground='turquoise1',bg='blue')
close7.place(x=660,y=20,height=30,width=30)
root6.overrideredirect(True)

root6.mainloop()
