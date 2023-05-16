import mysql.connector
import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
from PIL import ImageTk,Image

headlabelfont = ("Noto Sans CJK TC", 15, 'bold')

labelfont = ('Garamond', 14)

entryfont = ('Garamond', 12)

# My sql connection

mydb = mysql.connector.connect(

  host="localhost",
  user="root",
  password="12345",
  database="employee"


)
def submit():
    name1=Username.get()
    pass1=password.get()
    a="pankaj"
    b="smarty"
    if not name1 or not pass1:

       mb.showerror('Error!', "Please fill all the missing fields!!")
   
       
    if name1==a and pass1==(b):   
       # Preparing SQL query to INSERT a record into the database.
        cursor = mydb.cursor()  
        insert_stmt = (
           "INSERT INTO LO(USER,PASSWORD)"
           "VALUES (%s, %s)"
       )
        data = (name1,pass1)
           #executing the sql command
        cursor.execute(insert_stmt,data)

           #commit changes in databa  se

        mydb.commit()
        root.destroy()
        import NEWWITHWORKBENCH

    else:
         mb.showerror('Error!', "Please fill The right Detail !!")
      


def form():
    global root
    root = tk.Tk()
    root.geometry("800x800")
    root.configure(background="light pink")
    root.title("DBMS Login Page") 
    global  Username
    global password     
    Username=StringVar()
    password=StringVar()
   

    Label(root,bg ='light blue', text="LIBRARY MANAGEMENT SYSTEM " ,font=80).place(x=320,y=140)
    #name 
    canvas=Canvas(root,width=200,height=200)
    canvas.pack()
    img=ImageTk.PhotoImage(Image.open("p.jpg"))
    canvas.create_image(20,20,ANCHOR=NW,image=img)
    Label(root,bg ='light blue', text="USER  ID  ").place(x=320,y=240)
    #name textbox
    Entry(root, textvariable=Username).place(x=390,y=242)
    #contact Label
    Label(root,bg ='light blue', text="PASSWORD").place(x=320,y=300)
    #contact textbox
    Entry(root, textvariable=password).place(x=390,y=302)

 
    submitbtn = tk.Button(root, text ="Login",
                      bg ='light blue',command=submit)
    submitbtn.place(x = 320, y = 365, width = 55)

    root.mainloop()
form()