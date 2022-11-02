import tkinter as tk
from constant_values import *


root = tk.Tk()

spørsVindu = tk.Entry(root, font = ("Arial", 20))
spørsVindu.grid(row = 0, column = 0, columnspan = 4)
spørsVindu.config(state = "disabled")

svar1Button = tk.Button(root, text = "1", font = ("Arial, 20"),)
svar1Button.grid(row = 1, column = 0, sticky = "we")

svar2Button = tk.Button(root, text = "2", font = ("Arial, 20"),)
svar2Button.grid(row = 1, column = 1, sticky = "we")

svar3Button = tk.Button(root, text = "3", font = ("Arial, 20"),)
svar3Button.grid(row = 2, column = 0, sticky = "we")

svar4Button = tk.Button(root, text = "4", font = ("Arial, 20"),)
svar4Button.grid(row = 2, column = 1, sticky = "we")




root.mainloop()