from tkinter import *
import psycopg2
import tkinter as tk
import os
#from PIL import Image
#from PIL import ImageGrab
import pyautogui
from PIL import Image

rootR=tk.Tk()
rootR.geometry('1400x700+0+0')
imgbg=tk.PhotoImage(file="img\\img10.png")
img1=tk.PhotoImage(file="img\\flight6.png")
img2=tk.PhotoImage(file="img\\pass6.png")
img3=tk.PhotoImage(file="img\\pay2.png")
img4=tk.PhotoImage(file="img\\reset1.1.png")
img5=tk.PhotoImage(file="img\\btn10_1.png")
close5=tk.PhotoImage(file="img\\close7.png")

lbg=tk.Label(rootR,image=imgbg).pack()
lblusr=tk.Label(rootR,text='User:',bg='white',font='Arial 12')
lblusr.place(x=5,y=20,height=40,width=90)
txt=tk.Entry(rootR,font='Arial 12')
txt.place(x=5,y=65,height=40,width=120)

def View():

    canvas=tk.Canvas(rootR,bg='yellow')
    canvas.place(x=200,y=0,width=1000,height=700)

    can1=Label(canvas,bg='floral white')
    can1.place(x=20,y=10,width=950,height=180)

    lblFlight=Label(can1,bg='Blue',text='Flight Details',fg='white',font='Times 14 bold')
    lblFlight.place(x=0,y=0,width=950,height=40)
    lblFlightimg=Label(can1,bg='Blue',image=img1,fg='white',font='Times 14 bold')
    lblFlightimg.place(x=0,y=0,width=40,height=40)
    lblFlight1=Label(can1,bg='SkyBlue1',text='Flight\t\t\tDeparting\t\t\tArriving',fg='black',font='Times 12 italic')
    lblFlight1.place(x=0,y=40,width=950,height=25)

    can2=Label(canvas,bg='floral white')
    can2.place(x=20,y=200,width=950,height=300)

    lblpass=Label(can2,bg='Blue',text='Passenger(s) Details',fg='white',font='Times 14 bold')
    lblpass.place(x=0,y=0,width=950,height=40)
    lblpassimg=Label(can2,bg='Blue',image=img2,font='Times 14 bold')
    lblpassimg.place(x=0,y=0,width=40,height=40)
    lblpass1=Label(can2,bg='SkyBlue1',text='Sr.no\t\t\tPassenger Name\t\t\tType\t\t\tE-ticket No',fg='black',font='Times 12 italic')
    lblpass1.place(x=0,y=40,width=950,height=25)

    can3=Label(canvas,bg='floral white')
    can3.place(x=20,y=510,width=950,height=300)

    lblpay=Label(can3,bg='Blue',text='Payment Details',fg='white',font='Times 14 bold')
    lblpay.place(x=0,y=0,width=950,height=40)
    lblpayimg=Label(can3,bg='Blue',image=img3,fg='blue',font='Times 14 bold')
    lblpayimg.place(x=0,y=0,width=40,height=40)
    lblpay1=Label(can3,bg='SkyBlue1',text='Amount(INR)',fg='black',font='Times 12 italic')
    lblpay1.place(x=0,y=40,width=950,height=25)

    lblpay2=Label(can3,bg='white',text='Air Fare',fg='black',font='Arial 12 italic')
    lblpay2.place(x=20,y=70,width=200,height=25)
    lblpay3=Label(can3,bg='white',text='Taxes and fees',fg='black',font='Arial 12 italic')
    lblpay3.place(x=20,y=95,width=200,height=25)
    lblpay4=Label(can3,bg='white',text='Supplier GST',fg='black',font='Arial 12 italic')
    lblpay4.place(x=20,y=120,width=200,height=25)
    lblpay5=Label(can3,bg='white',text='Total',fg='black',font='Arial 12 bold')
    lblpay5.place(x=20,y=145,width=200,height=25)

    #retriving data to display
    con=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur1=con.cursor()
    cur2=con.cursor()
    cur3=con.cursor()
    cur1.execute("select * from PassengerDetails3")
    cur2.execute("select * from PassengerDetails1")
    cur3.execute("select * from FlightDetails")
    row1=cur1.fetchall()
    for i in row1:
        if((i[0]).lower()==txt.get().lower()):
            fname=i[1]
            Alist=i[2]
            Clist=i[3]
            break;
    print("fname",fname)
    listA1=Alist.split(',')
    print(listA1)
    str1=str(listA1)
    str2=str1.replace('{','')
    str3=str2.replace('}','')
    print("String3:",str3)
    L=str3.split(',')
    str4=str3.replace('[','')
    str5=str4.replace(']','')
    str6=str5.replace("'",'')
    print(str5)
    print(str6)
    A=str6.split(', ')
    #print(A[1])

    listC1=Clist.split(',')
    print(listC1)
    str7=str(listC1)
    str8=str7.replace('{','')
    str9=str8.replace('}','')
    print("String3:",str9)
    c11=str9.split(',')
    str10=str9.replace('[','')
    str11=str10.replace(']','')
    str12=str11.replace("'",'')
    print(str11)
    print(str12)
    C=str12.split(',')
    print(C)

    row2=cur2.fetchall()
    for i in row2:
        if((i[0]).lower()==txt.get().lower()):
            source=i[1]
            dest=i[2]
            adult=i[5]
            child=i[6]
            type1=i[8]
            class1=i[7]
            break;

    charges=0
    row3=cur3.fetchall()
    for i in row3:
        if((i[0]).lower()==fname.lower() and i[1]==source and i[2]==dest and i[5]==class1):
            charges=i[6]
            break;
    print(charges)
    amt1=int(adult)*int(charges)
    amt2=int(child)*int(charges)*0.8
    #amt=0
    amt=amt1+amt2
    print(amt)
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

    print(amt)
    #amt=amt+0.3*(int(charges))+0.05*(int(charges))

    #displaying details
    lblFly0=Label(can1,bg='floral white',text=fname,fg='black',font='Times 14 bold')
    lblFly0.place(x=200,y=65,width=100,height=40)
    lblFly1=Label(can1,bg='floral white',text=source,fg='black',font='Times 14 bold')
    lblFly1.place(x=400,y=65,width=100,height=40)
    lblFly2=Label(can1,bg='floral white',text=dest,fg='black',font='Times 14 bold')
    lblFly2.place(x=650,y=65,width=100,height=40)
    lblFly3=Label(can1,bg='floral white',text="Cabin:"+class1,fg='black',font='Times 14 bold')
    lblFly3.place(x=150,y=105,width=200,height=40)

    #can2
    p=70
    for k in range(0,len(A)):
        lblc2=Label(can2,bg='Blue',text=k,fg='white',font='Times 14 bold')
        lblc2.place(x=50,y=p,width=230,height=25)
        lblc21=Label(can2,bg='Blue',text=A[k-1],fg='white',font='Times 14 bold')
        lblc21.place(x=285,y=p,width=200,height=25)
        lblc22=Label(can2,bg='Blue',text="Adult",fg='white',font='Times 14 bold')
        lblc22.place(x=490,y=p,width=200,height=25)
        lblc23=Label(can2,bg='Blue',text=k+800,fg='white',font='Times 14 bold')
        lblc23.place(x=695,y=p,width=200,height=25)
        p=p+30

    q=p
    for m in range(len(C)):
        lblc2=Label(can2,bg='Blue',text=k+1,fg='white',font='Times 14 bold')
        lblc2.place(x=50,y=q,width=230,height=25)
        lblc21=Label(can2,bg='Blue',text=C[m-1],fg='white',font='Times 14 bold')
        lblc21.place(x=285,y=q,width=200,height=25)
        lblc22=Label(can2,bg='Blue',text="Child",fg='white',font='Times 14 bold')
        lblc22.place(x=490,y=q,width=200,height=25)
        lblc23=Label(can2,bg='Blue',text=m+900,fg='white',font='Times 14 bold')
        lblc23.place(x=695,y=q,width=200,height=25)
        q=q+30
        k=k+1

        
    
    #can3
    AirFare=amt
    fees=0.3*int(charges)
    GST=0.05*int(charges)
    Total=AirFare+fees+GST
    lblfare=Label(can3,bg='floral white',text=AirFare,fg='black',font='Times 14')
    lblfare.place(x=370,y=70,width=200,height=25)
    lblfee=Label(can3,bg='floral white',text=fees,fg='black',font='Times 14')
    lblfee.place(x=370,y=95,width=200,height=25)
    lblgst=Label(can3,bg='floral white',text=GST,fg='black',font='Times 14')
    lblgst.place(x=370,y=120,width=200,height=25)
    lbltotal=Label(can3,bg='floral white',text=Total,fg='black',font='Times 14 bold')
    lbltotal.place(x=370,y=145,width=200,height=25)
def ConvertToPdf():
    
    myScreenshot = pyautogui.screenshot()
    screenshotPath = r'C:\ss.png'
    myScreenshot.save(screenshotPath)

    image1 = Image.open(screenshotPath)
    im1 = image1.convert('RGB')
    pdfPath = r'C:\Flight_Receipt.pdf'
    im1.save(pdfPath)
    os.remove('C:\ss.png')

btn=tk.Button(rootR,text='View',font='Arial 12',command=View,image=img4,compound='center',bg='white',bd=0,fg='white',relief='solid')
btn.place(x=5,y=105,height=40,width=90)

btn1=tk.Button(rootR,text='Download Receipt',font='Arial 12',command=ConvertToPdf,image=img5,compound='center',bg='white',bd=0,fg='white',relief='solid')
btn1.place(x=5,y=205,height=60,width=180)

close=tk.Button(rootR,image=close5,bg='white',bd=0,highlightthickness=0,activebackground='SkyBlue',command=rootR.destroy)
close.place(x=1320,y=10,width=30,height=30)


rootR.overrideredirect(True)
rootR.mainloop()
