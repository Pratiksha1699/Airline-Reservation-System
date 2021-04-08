from tkinter import *
from tkinter import messagebox
import psycopg2

root1=Tk()
root1.geometry('800x500+30+40')
img1=PhotoImage(file="img\\image7.png")
img2=PhotoImage(file="img\\Sub2.png")
img3=PhotoImage(file="img\\close7.png")
w1=Label(root1,image=img1)
w1.pack()

def sub1():
    i=1
    print("Submitting Feedback")
    str1=txt.get('1.0',END)
    print("Str:",str1)
    conn=psycopg2.connect("dbname=travel user=postgres password=pratiksha host=localhost")
    cur=conn.cursor()
    cur.execute("insert into feedback values(%s,%s)",(str1,i))
    conn.commit()
    messagebox.showinfo(" ","Sucessfully saved Feedback!")
    
    
        
        
    
    

lbl0=Label(root1,text="Please fill suggestions or comments below:",font='Arial 15 bold',bg='OliveDrab1')
lbl0.place(x=20,y=30,width=500,height=50)
txt=Text(root1,bd=0,relief='solid',font="Arial 13",wrap=WORD)
txt.config(highlightbackground='white',highlightthickness=4,highlightcolor='Magenta')
txt.place(x=50,y=90,height=150)

B1=Button(root1,text="Submit",font='Arial 13 bold',relief='solid',bd=0,bg='dodger Blue2',compound="center",image=img2,command=sub1)
B1.place(x=350,y=350,width=80,height=55)
close7=Button(root1,image=img3,command=root1.destroy,relief='solid',bd=0,activebackground='turquoise1',bg='blue')
close7.place(x=750,y=20,height=30,width=30)
root1.overrideredirect(True)

root1.mainloop()
