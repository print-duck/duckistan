# Modern GUI with Python 
# pip install tkinter
import tkinter as tk
from tkinter import filedialog
r = tk.Tk()
# set title 
r.title("Medium GUI")
# set size
r.geometry("400x400")
# Create a label
label = tk.Label(r, text="Hello World")
label.place(x=10, y=10)
# Create a Inputbox
value = tk.StringVar()
inputbox = tk.Entry(r, textvariable=value)
inputbox.place(x=10, y=50)
# Create a Button
button = tk.Button(r, text="Click Me")
button.place(x=10, y=100)
# Checkboxes
opt1 = tk.IntVar()
check = tk.Checkbutton(r, text="Check Me", variable=opt1)
check.place(x=10, y=150)
# Import Image
img = tk.PhotoImage(file="catz.jpg")
image = tk.Label(r, image=img)
image.place(x=10, y=200)
# File Dialog
filedialog.askopenfilename(parent= r)
# run the app
r.mainloop()
