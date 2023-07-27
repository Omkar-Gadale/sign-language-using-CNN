import numpy as np
import os
import PIL
import cv2, pickle
from PIL import ImageTk
import PIL.Image
import speech_recognition as sr
import pyttsx3
from itertools import count
import string
from tkinter import *
import time
try:
    import Tkinter as tk
except:
    import tkinter as tk
import numpy as np
image_x, image_y = 64,64
from keras.models import load_model
classifier = load_model('model.h5')
def give_char():
       import numpy as np
       from keras.preprocessing import image
       test_image = image.load_img('tmp1.png', target_size=(64, 64))
       test_image = image.img_to_array(test_image)
       test_image = np.expand_dims(test_image, axis = 0)
       result = classifier.predict(test_image)
       print(result)
       chars="ABCDEFGHIJKMNOPQRSTUVWXYZ"
       indx=  np.argmax(result[0])
       print(indx)
       return(chars[indx])

def check_sim(i,file_map):
       for item in file_map:
              for word in file_map[item]:
                     if(i==word):
                            return 1,item
       return -1,""

op_dest="C:/Users/rohan/OneDrive/Desktop/two-way-sign-language-translator-master/two-way-sign-language-translator-master/filtered_data/"
alpha_dest="C:/Users/rohan/OneDrive/Desktop/two-way-sign-language-translator-master/two-way-sign-language-translator-master/alphabet/"
dirListing = os.listdir(op_dest)
editFiles = []
for item in dirListing:
       if ".webp" in item:
              editFiles.append(item)

file_map={}
for i in editFiles:
       tmp=i.replace(".webp","")
       #print(tmp)
       tmp=tmp.split()
       file_map[i]=tmp

def func(a):
       all_frames=[]
       final= PIL.Image.new('RGB', (380, 260))
       words=a.split()
       for i in words:
              flag,sim=check_sim(i,file_map)
              if(flag==-1):
                     for j in i:
                            print(j)
                            im = PIL.Image.open(alpha_dest+str(j).lower()+"_small.gif")
                            frameCnt = im.n_frames
                            for frame_cnt in range(frameCnt):
                                   im.seek(frame_cnt)
                                   im.save("tmp.png")
                                   img = cv2.imread("tmp.png")
                                   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                                   img = cv2.resize(img, (380,260))
                                   im_arr = PIL.Image.fromarray(img)
                                   for itr in range(15):
                                          all_frames.append(im_arr)
              else:
                     print(sim)
                     im = PIL.Image.open(op_dest+sim)
                     im.info.pop('background', None)
                     im.save('tmp.gif', 'gif', save_all=True)
                     im = PIL.Image.open("tmp.gif")
                     frameCnt = im.n_frames
                     for frame_cnt in range(frameCnt):
                            im.seek(frame_cnt)
                            im.save("tmp.png")
                            img = cv2.imread("tmp.png")
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            img = cv2.resize(img, (380,260))
                            im_arr = PIL.Image.fromarray(img)
                            all_frames.append(im_arr)
       final.save("out.gif", save_all=True, append_images=all_frames, duration=100, loop=0)
       return all_frames      

img_counter = 0
img_text=''
class Tk_Manage(tk.Tk):
       def __init__(self, *args, **kwargs):     
              tk.Tk.__init__(self, *args, **kwargs)
              container = tk.Frame(self)
              container.pack(side="top", fill="both", expand = True)
              container.grid_rowconfigure(0, weight=1)
              container.grid_columnconfigure(0, weight=1)
              self.frames = {}
              for F in (StartPage, VtoS, StoV):
                     frame = F(container, self)
                     self.frames[F] = frame
                     frame.grid(row=0, column=0, sticky="nsew")
              self.show_frame(StartPage)

       def show_frame(self, cont):
              frame = self.frames[cont]
              frame.tkraise()

        
class StartPage(tk.Frame):

       def __init__(self, parent, controller):
              tk.Frame.__init__(self,parent)
              label = tk.Label(self, text="Bidirectional Sign Language Translator", font=("Verdana", 12))
              label.pack(pady=20,padx=20)
              button = tk.Button(self,height = 2,width = 20, text="Text to Sign",command=lambda: controller.show_frame(VtoS))
              button.pack()
              button.place(x=300,y=90)
              button2 = tk.Button(self,height = 2,width = 20, text="Sign to Text",command=lambda: controller.show_frame(StoV))
              button2.pack()
              button2.place(x=550,y=90)
              load = PIL.Image.open("bi.png")
              load = load.resize((800, 500))
              render = ImageTk.PhotoImage(load)
              img = Label(self, image=render)
              img.image = render
              img.place(x=100, y=150) 
              


class VtoS(tk.Frame):
       def __init__(self, parent, controller):
              cnt=0
              gif_frames=[]
              inputtxt=None
              tk.Frame.__init__(self, parent)
              label = tk.Label(self, text="Text to Sign", font=("Verdana", 12))
              label.pack(pady=10,padx=10)
              gif_box = tk.Label(self)
              
              button1 = tk.Button(self,height = 2,width = 20, text="Back to Home",command=lambda: controller.show_frame(StartPage))
              button1.pack()
              button1.place(x=450,y=600)
             
    
              def gif_stream():
                     global cnt
                     global gif_frames
                     if(cnt==len(gif_frames)):
                            return
                     img = gif_frames[cnt]
                     cnt+=1
                     imgtk = ImageTk.PhotoImage(image=img)
                     gif_box.imgtk = imgtk
                     gif_box.configure(image=imgtk)
                     gif_box.after(50, gif_stream)
    
              
                                   
                                   
              def Take_input():
                     INPUT = inputtxt.get("1.0", "end-1c")
                     print(INPUT)
                     global gif_frames
                     gif_frames=func(INPUT)
                     global cnt
                     cnt=0
                     gif_stream()
                     gif_box.place(x=400,y=160)
              
              l = tk.Label(self,text = "Enter Text:")
              
              inputtxt = tk.Text(self, height = 4,width = 25)
              
              Display = tk.Button(self, height = 2,width = 20,text ="Convert",command = lambda:Take_input())
              Display.place(x=550,y=90)
              l.place(x=50, y=160)
              
              inputtxt.place(x=50, y=200)
              Display.pack()

def log():
    from subprocess import call
    call(["python","fun_util.py"])
class StoV(tk.Frame):
    

       def __init__(self, parent, controller):
              tk.Frame.__init__(self, parent)
              label = tk.Label(self, text="Sign to Text", font=("Verdana", 12))
             
              label.pack(pady=10,padx=10)
              button1 = tk.Button(self,height = 2,width = 20, text="Back to Home",command=lambda: controller.show_frame(StartPage))
              button1.pack()
              button1.place(x=450,y=600)
              button2 = tk.Button(self,height = 2,width = 20, text="Text to Sign",command=lambda: controller.show_frame(VtoS))
              button2.pack()
              button2.place(x=450,y=100)
              disp_txt = tk.Text(self, height = 4,width = 25)
              
              start = tk.Button(self,height = 2,width = 20, text="Sign to Text", command=log)
              start.place(x=450, y=200)


app = Tk_Manage()
app.geometry("1000x750")
app.mainloop()