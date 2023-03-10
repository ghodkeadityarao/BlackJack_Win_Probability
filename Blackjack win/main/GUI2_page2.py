import tkinter
from tkinter import messagebox
from tkinter import *
import random
import pandas as pd


window = tkinter.Tk()
window.title("Dealer + Player Cards")
window.geometry('1536x864')
window.configure(bg='#333333')


bg = PhotoImage(file = "D:\\Projects\\Blackjack win\\datasets\\img1.png")

labelimg = Label(window, image = bg)
frame = tkinter.Frame(bg='#333333')
# Creating widgets

label2 = tkinter.Label(frame, text="BlackJack Predictor", bg='#333333', fg="#FF3399", font=("Arial", 30))
label1 = tkinter.Label(frame, text="What You Know !?", bg='#333333', fg="#FF3399", font=("Arial", 20))
label3_line = tkinter.Label(frame, text="*****************", bg='#333333', fg="#FF3399", font=("Arial", 20))
deal = tkinter.StringVar()
option1_label = tkinter.Label(frame, text="Enter Dealer's First Card : " ,bg='#333333', fg="#FFFFFF", font=("Arial", 16))
option2_label = tkinter.Label(frame, text="Enter Your 2 Cards  ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
option3_label = tkinter.Label(frame, text="Enter Card 1 : ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
option4_label = tkinter.Label(frame, text="Enter Card 2 : ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
option5_label = tkinter.Label(frame, text="Sum : ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
option6_label = tkinter.Label(frame, text="STAND:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
option7_label = tkinter.Label(frame, text="HIT:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
dealercard_entry = tkinter.Entry(frame,textvariable=deal, font=("Arial", 16))
card1 = tkinter.StringVar()
card2 = tkinter.StringVar()
card1_entry = tkinter.Entry(frame,textvariable=card1 ,font=("Arial", 16))
card2_entry = tkinter.Entry(frame,textvariable=card2, font=("Arial", 16))
# Placing widgets on the screen
t1=tkinter.Text(frame,width=30,height=1.5, font=("Arial", 16))
t2=tkinter.Text(frame,width=85,height=3)
t3=tkinter.Text(frame,width=85,height=3)

def back():
    window.destroy()
    import GUI_homepage


def submit():
    c1 = card1.get()
    c2 = card2.get()
    d = deal.get()
    card_dic = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    sum = card_dic[c1] + card_dic[c2]
    t = str(sum)
    t1.insert(tkinter.END, t)
    
    df = pd.read_csv("D:\\Projects\\Blackjack win\\datasets\\Dataset2_clean.csv")
    z = card_dic[c1] + card_dic[c2]
    a = df.loc[df["sum"] == z][d]
    t2.insert(tkinter.END, a)

    df1 = pd.read_csv("D:\\Projects\\Blackjack win\\datasets\\Dataset3_clean.csv")
    r1 = c1+c2
    b = df1.loc[df1["sum1"] == r1][d]
    t3.insert(tkinter.END, b)

sub_btn=tkinter.Button(frame,width = 20 ,text = 'Submit', command = submit)
sub_btn1=tkinter.Button(frame,width = 20 ,text = 'Back', command = back)


labelimg.place(x = 150, y = 200)
label2.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
dealercard_entry.grid(row=9, column=1, pady=20)
card1_entry.grid(row=18, column=1, pady=20)
card2_entry.grid(row=21, column=1, pady=20)
t1.grid(row=24, column=1, pady=20)
t2.grid(row=27, column=1, pady=20)
t3.grid(row=35, column=1, pady=20)
label1.grid(row=1, column=0, columnspan=2, sticky="news", pady=10)
label3_line.grid(row=2, column=0, columnspan=2, sticky="news", pady=10)
option1_label.grid(row=9, column=0)
option2_label.grid(row=15, column=0, pady=5, columnspan=2)
option3_label.grid(row=18, column=0, pady=10)
option4_label.grid(row=21, column=0, pady=20)
option5_label.grid(row=24, column=0, pady=20)
option6_label.grid(row=27, column=0, pady=20)
option7_label.grid(row=35, column=0, pady=20)
sub_btn.grid(row=23, column=2)
sub_btn1.grid(row=24, column=2)

frame.pack()
window.mainloop()