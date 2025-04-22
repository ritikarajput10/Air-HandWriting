# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:10:04 2023

@author: COMPUTER
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:23:43 2021

@author: sheet
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author: om
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time


global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Air Handwritting using Machine learning ")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('A8.jpg')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)





#
label_l1 = tk.Label(root, text="Air Handwritting using Machine learning",font=("Times New Roman", 35, 'bold'),
                    background="#152238", fg="white", width=65, height=2)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])



def Air_writting():
    from subprocess import call
    call(["python","air_canvas_ml.py"])
    
def shape():
    from subprocess import call
    call(["python","virtual_shape.py"])
    
def number():
    from subprocess import call
    call(["python","draw.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Air_writting", command=Air_writting, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=160)

button1 = tk.Button(root, text="Shape", command=shape, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=330)

button1 = tk.Button(root, text="number", command=number, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=440)



button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=100, y=550)

root.mainloop()