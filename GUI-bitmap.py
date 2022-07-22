import tkinter as tk
from tkinter import*

#  bitmap= " error","gray75","gray50","gray25","gray12","hourglass","info","questhead","question","warning"




window=tk.Tk()



window.geometry("300x300")


b=Button(bitmap="questhead")
b.place(x=10,y=10)










window.mainloop()