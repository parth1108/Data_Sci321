from tkinter import *

root=Tk(className=" Welcome to the Registration ")

root.geometry('300x300')

a = Label(root,text='Personal Information',fg='Red',font='Helvetica 15 bold').place(x=40,y=20)

x = Label(root,text='First Name').place(x=20,y=50)
x1 = Label(root,text='Middle Name').place(x=20,y=80)
x2 = Label(root,text='Last Name').place(x=20,y=110)

y = Entry(width=20).place(x=100,y=50)
y1 = Entry(width=20).place(x=100,y=80)
y2 = Entry(width=20).place(x=100,y=110)

root.mainloop()