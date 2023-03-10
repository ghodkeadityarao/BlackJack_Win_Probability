import tkinter
from tkinter import *
import os
import pandas as pd


window = tkinter.Tk()
window.title("Dealer Card")
window.geometry('1536x864')
window.configure(bg='#333333')


bg = PhotoImage(file = "D:\\Projects\\Blackjack win\\datasets\\img1.png")

labelimg = Label(window, image = bg)
frame = tkinter.Frame(bg='#333333')

# Creating widgets
card1 = tkinter.StringVar()

label2 = tkinter.Label(frame, text="BlackJack Predictor", bg='#333333', fg="#FF3399", font=("Arial", 30))
label1 = tkinter.Label(frame, text="What You Know !?", bg='#333333', fg="#FF3399", font=("Arial", 20))
label3_line = tkinter.Label(frame, text="*****************", bg='#333333', fg="#FF3399", font=("Arial", 20))
option1_label = tkinter.Label(frame, text="Enter Dealer's First Card : ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, textvariable = card1,font=("Arial", 16))

t1=tkinter.Text(frame,width=85,height=3)
t1.grid(row=90, column=0, columnspan=2, sticky="news", pady=15)

def back():
    window.destroy()
    import GUI_homepage

def submit():
    c = card1.get()
    df = pd.read_csv("D:\\Projects\\Blackjack win\\datasets\\Dataset1_clean.csv")
    a = df.loc[df["card"] == c]
    t1.insert(tkinter.END, a)

sub_btn=tkinter.Button(frame,width = 20 ,text = 'Submit', command = submit)
sub_btn1=tkinter.Button(frame,width = 20 ,text = 'Back', command = back)

labelimg.place(x = 150, y = 200)
label2.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
username_entry.grid(row=9, column=1, pady=20)
label1.grid(row=1, column=0, columnspan=2, sticky="news", pady=10)
label3_line.grid(row=2, column=0, columnspan=2, sticky="news", pady=10)
option1_label.grid(row=9, column=0)
sub_btn.grid(row=14, column=0)
sub_btn1.grid(row=14, column=1)

frame.pack()
window.mainloop()