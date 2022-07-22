from tkinter import *
import tkinter as tk



window=tk.Tk()
window.geometry("300x300")


image=PhotoImage(file="bahçe.gif")


kimage=image.subsample(5,5) #resmi 5 kat küçültür



b=Button(text="Oyun",image=kimage,compound=LEFT) #compound resim yazının sağında mı yoksa solunda mı olucak
b.place(x=10,y=10)



window.mainloop()