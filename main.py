import tkinter as tk
from constant_values import *
import os
def turn_off():
    os.system('shutdown -p')

questions = ("Får kevin bitches?", "Får jørgen bitches?", "Får Egil bitches?")

answers = [(("ja", 0), ("nei", 1), ("noen", 0),("All the bitches", 0)),
           (("ja", 0), ("nei", 0), ("noen", 1),("All the bitches", 0)),
           (("ja", 0), ("nei", 0), ("noen", 0),("All the bitches", 1))]


def display_new():
    num = _num.get()
    q = questions[num]
    spørsVindu.config(state= "normal")
    spørsVindu.insert(0, q)
    spørsVindu.config(state= "disabled")
    svar1Button.config(text = answers[num][0][0])
    svar2Button.config(text = answers[num][1][0])
    svar3Button.config(text = answers[num][2][0])
    svar4Button.config(text = answers[num][3][0])


#kontrollerer om svaret er rett

def button1_pressed():
    num = _num.get()
    _num.set(_num.get()+1)
    if answers[num][0][1] == 1 :
        pass
    else:
        turn_off()

def button2_pressed():
    num = _num.get()
    _num.set(_num.get()+1)
    if answers[num][1][1] == 1 :
        pass
    else:
        turn_off()

def button3_pressed():
    num = _num.get()
    _num.set(_num.get()+1)
    if answers[num][2][1] == 1 :
        pass
    else:
        turn_off()

def button4_pressed():
    num = _num.get()
    _num.set(_num.get()+1)
    if answers[num][3][1] == 1 :
        pass
    else:
        turn_off()




root = tk.Tk()
_num = tk.IntVar()
_num.set(0)
spørsVindu = tk.Entry(root, font = large_font,)
spørsVindu.grid(row = 0, column = 0, columnspan = 4)
spørsVindu.config(state = "disabled")

svar1Button = tk.Button(root, text = "1", font = liten_font, command = button1_pressed)
svar1Button.grid(row = 1, column = 0, sticky = "we")

svar2Button = tk.Button(root, text = "2", font = liten_font,command = button2_pressed)
svar2Button.grid(row = 1, column = 1, sticky = "we")

svar3Button = tk.Button(root, text = "3", font = liten_font,command = button3_pressed)
svar3Button.grid(row = 2, column = 0, sticky = "we")

svar4Button = tk.Button(root, text = "4", font = liten_font,command = button4_pressed)
svar4Button.grid(row = 2, column = 1, sticky = "we")



display_new()
root.mainloop()