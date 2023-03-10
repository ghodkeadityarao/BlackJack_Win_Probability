import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

window = tkinter.Tk()
window.title("Blackjack Prediction")
window.geometry('1536x864')
window.configure(bg='#333333')

def open_file_1():
    window.destroy()
    import GUI1_page1
def open_file_2():
    window.destroy()
    import GUI2_page2
bg = PhotoImage(file = "D:\\Projects\\Blackjack win\\datasets\\img1.png")

labelimg = Label(window, image = bg)
frame = tkinter.Frame(bg='#333333')


# Creating widgets
label2 = tkinter.Label(frame, text="BlackJack Predictor", bg='#333333', fg="#FF3399", font=("Narkisim", 30))
label1 = tkinter.Label(frame, text="What You Know !?", bg='#333333', fg="#FF3399", font=("Arial", 20))
label3_line = tkinter.Label(frame, text="*****************", bg='#333333', fg="#FF3399", font=("Arial", 20))

option1_label = tkinter.Label(frame, text="Option 1: ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
option2_label = tkinter.Label(frame, text="Option 2: ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
option1_button = tkinter.Button(frame, text="Dealer's First Card.", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=open_file_1)
option2_button = tkinter.Button(frame, text="Dealer's First Card + Your 2 Cards.", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=open_file_2)

# Placing widgets on the screen
labelimg.place(x = 150, y = 200)
label2.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
label1.grid(row=1, column=0, columnspan=2, sticky="news", pady=10)
label3_line.grid(row=3, column=0, columnspan=2, sticky="news", pady=10)
option1_label.grid(row=4, column=0)
option2_label.grid(row=5, column=0)
option1_button.grid(row=4,column=1,pady=20)
option2_button.grid(row=5,column=1,pady=20)

frame.pack()
window.mainloop()
