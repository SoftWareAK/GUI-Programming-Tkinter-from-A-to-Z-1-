import tkinter as tk
from tkinter import *
def sec1():
    print("Seçim 1",c1.get())

def sec2():
    print("Seçim 2",c2.get())
def rsec():
    print(r.get())




pencere =tk.Tk()
pencere.geometry("300x300")

c1=IntVar()
c2=IntVar()

cb1=Checkbutton(text="secim1", variable=c1,onvalue=1,offvalue=0,command=sec1)
cb2=Checkbutton(text="secim2", variable=c2,onvalue=1,offvalue=0,command=sec2)
cb1.place(x=20,y=20)
cb2.place(x=100,y=20)


r=IntVar()



rb1=Radiobutton(text="Radıo1",variable=r,value=1,command=rsec)
rb2=Radiobutton(text="Radıo2",variable=r,value=2,command=rsec)
rb1.place(x=20,y=50)
rb2.place(x=100,y=50)


pencere.mainloop()