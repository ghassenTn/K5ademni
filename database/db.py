from tkinter import *
root = Tk()
root.geometry("1100x550+100+40")
root.resizable(False,False)
root.configure(background="white")
root.title('خدمني [Data base] Controlles V1.0 ')
Tittle = Label (root,text="Database Controlls V1.0 Sql server",bg="blue",fg="black")
Tittle.pack(fill=X)
f1 = Frame(root,bg="whitesmoke",bd=2,relief=GROOVE)
f1.place(x=5,y=27,width=350,height=220)
Tittle1 = Label (f1,text="Database Controlls ",bg="whitesmoke",fg="black")
Tittle1.pack(fill=X)
l = Label(f1,text="Show all Data bases",fg="blue")
l.place(x=10,y=50)
b1 = Button(f1,text="All Data Bases",cursor="hand2",bg="#4ade80")
b1.place(x=130,y=47)
b2 =Button(f1,text="Hide",bg="#a8a29e",cursor="hand2",width=7)
b2.place(x=220,y=47)
l1 = Label(f1,text="db names :",fg="blue")
l1.place(x=10,y=100)
ent= Entry(f1)
ent.place(x=90,y=103)
b3=Button(f1,text="Create Data base",bg="#a8a29e",cursor="hand2",width=15)
b3.place(x=220,y=101)
l2 = Label(f1,text="Table coluns:",fg="blue")
l2.place(x=10 , y=140)
b3=Button(f1,text="Create Table",bg="#a8a29e",cursor="hand2",width=15)
b3.place(x=90,y=140)
b3=Button(f1,text="hide",bg="#a8a29e",cursor="hand2",width=15)
b3.place(x=220,y=101)

root.mainloop()
