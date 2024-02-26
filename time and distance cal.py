from tkinter import *
from tkinter import messagebox

w = Tk()
w.geometry("400x400")
w.config(bg="#116562")
w.title("time|distance calculator")

def hour(e,e2):
    if e==""or e2=="":
        messagebox.showerror("None" , "there is no value to calculate !")
    elif 0<float(e) or 0>float(e) or 0<float(e2)or 0>float(e2):
        res = float(e)/float(e2)
        r.delete(0,END)
        r.insert(0," hour")
        r.insert(0,res)
    else:
        messagebox.showerror("Error" , "it shouldn't be zero")
    return

def min(e,e2):
    if e==""or e2=="":
        messagebox.showerror("None" , "there is no value to calculate !")
    elif 0<float(e) or 0>float(e) or 0<float(e2)or 0>float(e2):
        res = float(e)/float(e2)*60
        r.delete(0,END)
        r.insert(0, " min")
        r.insert(0,res)
    else:
        messagebox.showerror("Error" , "it shouldn't be zero")
    return
    
def speed(e,e3):
    if e==""or e3=="":
        messagebox.showerror("None" , "there is no value to calculate !")
    elif 0<float(e) or 0>float(e) or 0<float(e3)or 0>float(e3):
        re = float(e)/float(e3)
        r.delete(0,END)
        r.insert(0," km/h")
        r.insert(0,re)
    else:
        messagebox.showerror("Error" , "it shouldn't be zero")
  
    return


lab1 = Label(w, text= " distance km").place(x=25,y=30)
lab2 = Label(w, text= "speed km/h ").place(x=25, y=100)
lab3 = Label(w, text= "time h ").place(x=25,y=170)
result = Label(w, text= "result",font=(4)).place(x=165,y=220)

num1 = IntVar()
e = Entry(w, textvariable=num1,justify=CENTER)
e.place(x=250,y=30)
e.delete(0,END)
num2 = IntVar()
e2 = Entry(w, textvariable=num2,justify=CENTER)
e2.place(x=250,y=100)
e2.delete(0,END)
num3 = IntVar()
e3 = Entry(w, textvariable=num3,justify=CENTER)
e3.place(x=250,y=170)
e3.delete(0,END)

r = Entry(w,justify=CENTER,width=21,borderwidth=4)
r.place(x=125,y=250)

b1 = Button(w, text="find hours ",padx=25,pady=8, command=lambda:hour(e.get(),e2.get())).place(x=140,y=300)
b2 = Button(w, text="find minute",padx=25,pady=8, command=lambda:min(e.get(),e2.get())).place(x=270,y=300)
b3 = Button(w, text="find speed ",padx=25,pady=8, command=lambda:speed(e.get(),e3.get())).place(x=10,y=300)

b_exit = Button(w, text="Exit", command=w.quit)
b_exit.place(x=370,y=375)



w.mainloop()