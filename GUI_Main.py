# -*- coding: utf-8 -*-
s
from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title("Sign Detection Using Machine Learning")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")

bg = Image.open(r"2.jpg")
bg.resize((1800,900),Image.ANTIALIAS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="Sign Detection Using Machine Learning",width=40,background="skyblue",height=2,font=("Times new roman",25,"bold"))
w.place(x=0,y=0)

def Login():
    from subprocess import call
    call(["python","Login.py"])
def Register():
    from subprocess import call
    call(["python","Registration.py"])

def Exit():
    root.destroy()


wlcm=tk.Label(root,text="...... Welcome to Sign Detection Using Machine Learning ......",width=60,height=3,background="skyblue",foreground="black",font=("Times new roman",15,"bold"))
wlcm.place(x=450,y=150)
        
btn_log=tk.Button(root,text="Login",command=Login,width=15,font=("Times new roman", 14, "bold"),bg="white",fg="black")
btn_log.place(x=1100,y=30)
btn_reg=tk.Button(root,text="Register",command=Register,width=15,font=("Times new roman", 14, "bold"),bg="white",fg="black")
btn_reg.place(x=1300,y=30)
btn_reg=tk.Button(root,text="Exit",command=Exit,width=15,font=("Times new roman", 14, "bold"),bg="white",fg="black")
btn_reg.place(x=20,y=700)



root.mainloop()
