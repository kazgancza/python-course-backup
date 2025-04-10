import tkinter as tk
import os

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

window = tk.Tk()
window.title("Application")
logo = tk.PhotoImage(file="img.png")


label1 = tk.Label(window,
                  text = "Line 1",
                  foreground = "white",
                  background = "black",
                  width = 20,
                  height = 5,
                  cursor = "dot",
                  font = "Times 18 bold italic underline",
                  anchor = tk.W,
                  padx = 15,
                  pady = 10
                  )
label1.pack()

label2 = tk.Label(window, text = "Line 2")
label2.pack()

label3 = tk.Label(window,
                  text="Line 3",
                  image=logo,
                  width=200,
                  height=200,
                  
                  compound=tk.CENTER)
label3.pack()

window.mainloop()
