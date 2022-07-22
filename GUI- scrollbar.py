import tkinter as tk
from tkinter import *


pencere=tk.Tk()

scroll=Scrollbar()
scroll.pack(side=RIGHT,fill=Y)
liste=Listbox(yscrollcommand=scroll.set)
for i in range(100):
    liste.insert(END,str(i)+". satır")


liste.pack(side=LEFT,fill=BOTH)
scroll.config(command=liste.yview)

pencere.mainloop()