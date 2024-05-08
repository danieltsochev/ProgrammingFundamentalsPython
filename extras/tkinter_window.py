from tkinter import *

import tkinter as tk

root = tk.Tk()

root.geometry("400x450")
root.title("Daniel's Notebook")
root.configure(bg="purple")

label = tk.Label(root, text="Hello Daniel", font=('Arial', 15))
label.pack(padx=20, pady=20)
label.configure(bg="purple")

textbox = tk.Text(root, height=5,  font=('Arial', 16))
textbox.pack(padx=50, pady=50)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)


btn1 = tk.Button(buttonframe, text="How To Use", font=('Arial', 20))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="Add Task", font=('Arial', 20))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="Delete Tasks", font=('Arial', 20))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="Show Tasks", font=('Arial', 20))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="Tasks Done", font=('Arial', 20))
btn4.grid(row=1, column=1, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="Analysis", font=('Arial', 20))
btn4.grid(row=1, column=2, sticky=tk.W+tk.E)


buttonframe.pack()
root.mainloop()