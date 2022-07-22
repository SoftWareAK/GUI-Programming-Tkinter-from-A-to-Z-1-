import tkinter as tk
from tkinter.ttk import *

def secimAl():
    print(combo.get())


pencere=tk.Tk()
pencere.geometry("300x300")
combo=Combobox()
combo['values']=("İstanbul","Antalya","Alanya","Manavgat","Güzelbağ")
combo.current(2) #,değerlerden 2 numarada olanı seçer
combo.place(x=20,y=20)

button=tk.Button(text="işlem",command=secimAl)
button.place(x=20,y=60)

pencere.mainloop()