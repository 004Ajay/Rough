from tkinter import *
import sys
import time

global count
count=0
class countertimer():
    def __init__(self):
            super().__init__()
            self.root=Tk()
            self.root.title("Counter Timer Watch")
            self.root.geometry("600x200")
            self.t=StringVar()
            self.t.set("00:00:00")
            self.lb=Label(self.root,textvariable=self.t,font=("Times 40 bold"),bg="#90FF92")
            self.start=Button(self.root,text="Start",command=self.start,font=("Times 12 bold"),bg="#F8FFED")
            self.pause=Button(self.root,text="Pause",command=self.pause,font=("Times 12 bold"),bg="#F8FFED")
            self.resume=Button(self.root,text="Resume",command=self.resume,font=("Times 12 bold"),bg="#F8FFED")
            self.reset=Button(self.root,text="Reset",command=self.reset,font=("Times 12 bold"),bg="#F8FFED")
            self.lb.place(x=160,y=100)
            self.start.place(x=120,y=100)
            self.pause.place(x=220,y=100)
            self.resume.place(x=320,y=100)
            self.reset.place(x=420,y=100)
            self.label=Label(self.root,text="",font=("Times 40 bold"))
            self.root.configure(bg='#90FF92')
    def reset(self):
        global count
        count=1
        self.pause['state']='disabled'
        self.start['state']='normal'
        self.resume['state']='disabled'
        self.reset['state']='disabled'
        self.t.set('00:00:00')
        
    def start(self):
        global count
        count=1
        self.start['state']='disabled'
        self.resume['state']='disabled'
        self.pause['state']='normal'
        self.reset['state']='disabled'
        self.timer()
    
    def pause(self):
        global count
        count=1
        self.start['state']='disabled'
        self.resume['state']='normal'
        self.pause['state']='disabled'
        self.reset['state']='normal'

    def resume(self):
        global count
        count=1
        self.start['state']='disabled'
        self.resume['state']='disabled'
        self.pause['state']='normal'
        self.reset['state']='disabled'
        self.timer()
    
    def timer(self):
        global count
        if count==0:
            self.d=str(self.t.get())
            hr,min,sec = map(int,self.d.split(":"))
            hr=int(hr)
            min=int(min)
            sec=int(sec)
            if sec<59:
                s+=1
            elif s==59:
                sec=0
                if min<59:
                    min+=1
                elif min==59:
                    min=0
                    hr+=1
            if hr<10:
                hr=str(0)+str(hr)
            else:
                hr=str(hr)
            if min<10:
                min=str(0)+str(min)
            else:
                min=str(min)
            if sec<10:
                sec=str(0)+str(sec)
            else:
                sec+str(sec)
            self.d=hr+":"+min+":"+sec
            self.t.set(self.d)
            if count==0:
                self.root.after(1000,self.timer)
        
    
            
if __name__ == '__main__':
    app = countertimer()
    app.mainloop()