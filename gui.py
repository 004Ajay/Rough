from tkinter import *

root = Tk()
root.geometry('500x500')

lbl1 = Label(root, text='Certificate Generator', font=('Montserrat', 20))
lbl1.pack(anchor=CENTER)

link_lbl = Label(root, text='Dest. Folder Link', font=('Montserrat', 12))
link_lbl.place(x=100, y=150)
link_entry = Entry(root,font=('Montserrat',10),bg='white')
link_entry.place(x=200, y=250, width=100)

btn1 = Button(root, text="Next", font=('Montserrat', 20))
btn1.pack(side=BOTTOM) 

root.mainloop()