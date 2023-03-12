from tkinter import *
import sys
import os
import datetime
window = Tk()
window.title("SpiraloVersion-2")
window.geometry("1000x1000")
bg = PhotoImage(file='C:/Users/Shakthi/Downloads/Restaurant-PNG-File-Download-Free.png')
l17 = Label(window, image=bg)
l17.pack()
x=Label(window,text="franchise vegrest.x",font="timesbold28",fg="black")
x.pack()
y=Label(window,text="Veg-Starters",font="timesbold28",fg="black",bg="white")
y.place(x=10,y=50)
sb = Scrollbar(window,orient=VERTICAL)
sb.pack()
label1 = Label(window, text="Chilli PotatoRs 50",font="times 18",fg="black",bg="white")
label1.place(x=10, y=100)
e1=Entry(window)
e1.place(x=10,y=150)
label2 = Label(window, text="Gobi65-Rs80",font="times 18",fg="black",bg="white")
label2.place(x=10, y=200)
e2=Entry(window)
e2.place(x=10,y=250)
label3 = Label(window, text="Paneer65-Rs70",font="times 18",fg="black",bg="white")
label3.place(x=10, y=300)
e3=Entry(window)
e3.place(x=10,y=350)
label4 = Label(window, text="French Fries-Rs90",font="times 18",fg="black",bg="white")
label4.place(x=10, y=400)
e4=Entry(window)
e4.place(x=10,y=450)
label5 = Label(window, text="Mushroom65-Rs100",font="times 18",fg="black",bg="white")
label5.place(x=10, y=500)
e5=Entry(window)
e5.place(x=10,y=550)
a=Label(window,text="Chinese cuisine",font="timesbold28",fg="black",bg="white")
a.place(x=300,y=50)
a1=Label(window, text="Fried rice-Rs 50",font="times 18",fg="black",bg="white")
a1.place(x=300,y=90)
e6=Entry(window)
e6.place(x=300,y=140)
a2=Label(window,text="Veg.Noodles-Rs 50",font="times 18",fg="black",bg="white")
a2.place(x=300,y=190)
e7=Entry(window)
e7.place(x=300,y=240)
a3=Label(window,text="Schezwan Fried rice-Rs 70",font="times 18",fg="black",bg="white")
a3.place(x=300,y=290)
e8=Entry(window)
e8.place(x=300,y=340)
a4=Label(window,text="Schezwan Noodles-Rs 70",font="times 18",fg="black",bg="white")
a4.place(x=300,y=390)
e9=Entry(window)
e9.place(x=300,y=440)
a5=Label(window,text="Malai-Kofta-Rs 150",font="times 18",fg="black",bg="white")
a5.place(x=300,y=490)
e10=Entry(window)
e10.place(x=300,y=540)
b=Label(window,text="Punjabifoodz ",font="timesbold28",fg="black",bg="white")
b.place(x=600,y=50)
b1=Label(window,text="Butternaan-Rs30",font="times 18",fg="black",bg="white")
b1.place(x=600,y=100)
e11=Entry(window)
e11.place(x=600,y=150)
b2=Label(window,text="Garlicnaan-Rs35",font="times 18",fg="black",bg="white")
b2.place(x=600,y=200)
e12=Entry(window)
e12.place(x=600,y=250)
b3=Label(window,text="Kulcha-Rs30",font="times 18",fg="black",bg="white")
b3.place(x=600,y=300)
e13=Entry(window)
e13.place(x=600,y=350)
b4=Label(window,text="Paneertikka-Rs60",font="times 18",fg="black",bg="white")
b4.place(x=600,y=400)
e14=Entry(window)
e14.place(x=600,y=450)
b5=Label(window,text="Dal makni-Rs60",font="times 18",fg="black",bg="white")
b5.place(x=600,y=500)
e15=Entry(window)
e15.place(x=600,y=550)
c=Label(window,text="Indian cuisine",font="timesbold28",fg="black",bg="white")
c.place(x=800,y=50)
c1=Label(window,text="Veg briyani-Rs100",font="times18",fg="black",bg="white")
c1.place(x=800,y=100)
e16=Entry(window)
e16.place(x=800,y=150)
c2=Label(window,text="Mushroombriyani-Rs120",font="times18",fg="black",bg="white")
c2.place(x=800,y=200)
e17=Entry(window)
e17.place(x=800,y=250)
c3=Label(window,text="North Indian thali-Rs100",font="times18",fg="black",bg="white")
c3.place(x=800,y=300)
e18=Entry(window)
e18.place(x=800,y=350)
c4=Label(window,text="South Indian thali-Rs100",font="times18",fg="black",bg="white")
c4.place(x=800,y=400)
e19=Entry(window)
e19.place(x=800,y=450)
c5=Label(window,text="Special combo-Rs150",font="times18",fg="black",bg="white")
c5.place(x=800,y=500)
e20=Entry(window)
e20.place(x=800,y=550)
d=Label(window,text="Rice and Roti",font="timesbold28",fg="black",bg="white")
d.place(x=1100,y=50)
d1=Label(window,text="Jeera rice-Rs100",font="times18",fg="black",bg="white")
d1.place(x=1100,y=100)
e21=Entry(window)
e21.place(x=1100,y=150)
d2=Label(window,text="Rice-Rs50",font="times18",fg="black",bg="white")
d2.place(x=1100,y=200)
e22=Entry(window)
e22.place(x=1100,y=250)
d3=Label(window,text="Dal rice-Rs90",font="times18",fg="black",bg="white")
d3.place(x=1100,y=300)
e23=Entry(window)
e23.place(x=1100,y=350)
d4=Label(window,text="Roti-Rs15",font="times18",fg="black",bg="white")
d4.place(x=1100,y=400)
e24=Entry(window)
e24.place(x=1100,y=450)
d5=Label(window,text="Phulka-Rs20",font="times18",fg="black",bg="white")
d5.place(x=1100,y=500)
e25=Entry(window)
e25.place(x=1100,y=550)    
def calculate():
    dic = {'Chilli PotatoRs 50': [e1, 50],
               'Gobi65-Rs80':[e2,80],
               'Paneer65-Rs70':[e3,70],
               'French Fries-Rs90':[e4,90],
               'Mushroom65-Rs100':[e5,100],
               'Fried rice-Rs 50':[e6,50],
               'Veg.Noodles-Rs 50':[e7,50],
               'Schezwan Fried rice-Rs 70':[e8,70],
               'Schezwan Noodles-Rs 70':[e9,70],
               'Malai-Kofta-Rs 150':[e10,150],
               'Butternaan-Rs30':[e11,30],
               'Garlicnaan-Rs35':[e12,35],
               'Kulcha-Rs30':[e13,30],
               'Paneertikka-Rs60':[e14,60],
               'Dal makni-Rs60':[e15,60],
               'Veg briyani-Rs100':[e16,100],
               'Mushroombriyani-Rs120':[e17,120],
               'North Indian thali-Rs100':[e18,100],
               'South Indian thali-Rs100':[e19,100],
               'Special combo-Rs150':[e20,150],
               'Jeera rice-Rs100':[e21,100],
               'Rice-Rs50':[e22,50],
               'Dal rice-Rs90':[e23,90],
               'Roti-Rs15':[e24,15],
               'Phulka-Rs20':[e25,20]}
    total = 0
    for key, val in dic.items():
        if val[0].get() != "":
            total += int(val[0].get())*val[1]
    label16 = Label(window,
                    text="Your Total Bill is Rs - "+str(total),
                    font="times 18")
    label16.place(x=20, y=600)
    label16.after(1000, label16.destroy)
    window.after(1000, calculate)
window.after(1000, calculate)
window.mainloop()
