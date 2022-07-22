import tkinter as tk

def topla():
    s1=int(sayi1.get())
    s2=int(sayi2.get())
    sonuc['text']=str(s1+s2)

def cikar():
    s1=int(sayi1.get())
    s2=int(sayi2.get())
    sonuc['text']=str(s1-s2)

def carp():
    s1=int(sayi1.get())
    s2=int(sayi2.get())
    sonuc['text']=str(s1*s2)

def bol():
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc['text']=str(s1/s2)


#pencere
pencere=tk.Tk()
pencere.geometry("300x150")
pencere.configure(bg="gray")
pencere.title("Ahmet's calculator")

sayi1=tk.Entry(width=10)
sayi1.place(x=20,y=20)

sayi2=tk.Entry(width=10)
sayi2.place(x=100,y=20)

sonuc=tk.Label(text="Sonuc",bg="blue")
sonuc['font'] = "Verdana 12 bold"
sonuc['fg'] = '#000000'   #hex code renk tanımlamasını kabul eder
sonuc.place(x=180,y=20)

btopla=tk.Button(text="+",bg="blue",font="Verdana 18 bold",command=topla).place(x=20,y=50)
bcikar=tk.Button(text="-",bg="blue",font="Verdana 18 bold",command=cikar).place(x=80,y=50)
bcarp=tk.Button(text="x",bg="blue",font="Verdana 18 bold",command=carp).place(x=140,y=50)
bbol=tk.Button(text="/",bg="blue",font="Verdana 18 bold",command=bol).place(x=200,y=50)



pencere.mainloop()
