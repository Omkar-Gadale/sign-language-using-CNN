# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:21:19 2023

@author: PC_POISON
"""

import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
# import os
# import cv2


window = tk.Tk()
window.configure(background="white")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
window.title("REGISTRATION FORM")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()

value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            window.destroy()
            from subprocess import call
            call(["python", "GUI_Master.py"])

#####################################################################################################################################################

#from subprocess import call
#call(["python", "lecture_login.py"])


# assign and define variable
# def login():

#####For background Image
image2 = Image.open('3.png')
image2 = image2.resize((1200,850), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=500, y=0)  # , relwidth=1, relheight=1)

Registration_frame=tk.Frame(window,bg="skyblue")
Registration_frame.place(x=100,y=30, width=500, height=730)
logolbl=tk.Label(Registration_frame,text="Registration Form", font=("Times new roman", 30, "bold"), bg="#192841", fg="white",bd=0).place(x=100,y=30)

# that is for label1 registration

l2 = tk.Label(Registration_frame, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=50, y=120)
t1 = tk.Entry(Registration_frame, textvar=Fullname, width=20, font=('', 15))
t1.place(x=240, y=120)
# that is for label 2 (full name)


l3 = tk.Label(Registration_frame, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l3.place(x=50, y=170)
t2 = tk.Entry(Registration_frame, textvar=address, width=20, font=('', 15))
t2.place(x=240, y=170)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(Registration_frame, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l5.place(x=50, y=220)
t4 = tk.Entry(Registration_frame, textvar=Email, width=20, font=('', 15))
t4.place(x=240, y=220)
# that is for email address

l6 = tk.Label(Registration_frame, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l6.place(x=50, y=270)
t5 = tk.Entry(Registration_frame, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=240, y=270)
# phone number
l7 = tk.Label(Registration_frame, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l7.place(x=50, y=320)
# gender
tk.Radiobutton(Registration_frame, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=var, value=1).place(x=240,
                                                                                                                y=320)
tk.Radiobutton(Registration_frame, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=var, value=2).place(
    x=350, y=320)

l8 = tk.Label(Registration_frame, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l8.place(x=50, y=370)
t6 = tk.Entry(Registration_frame, textvar=age, width=20, font=('', 15))
t6.place(x=240, y=370)

l4 = tk.Label(Registration_frame, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l4.place(x=50, y=420)
t3 = tk.Entry(Registration_frame, textvar=username, width=20, font=('', 15))
t3.place(x=240, y=420)

l9 = tk.Label(Registration_frame, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l9.place(x=50, y=470)
t9 = tk.Entry(Registration_frame, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=240, y=470)

l10 = tk.Label(Registration_frame, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"), bg="snow")
l10.place(x=50, y=520)

t10 = tk.Entry(Registration_frame, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=240, y=520)

btn = tk.Button(Registration_frame, text="Register", bg="#192841",font=("",20),fg="white", width=9, height=1, command=insert)
btn.place(x=180, y=590)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()