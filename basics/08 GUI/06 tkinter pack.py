import tkinter as tk

window = tk.Tk()

label1=tk.Label(window, text="Label1", bg="red")
label1.pack(side=tk.TOP, expand=True, fill=tk.Y)
label2=tk.Label(window, text="Label2")
label2.pack()
label3=tk.Label(window, text="Labe3", bg="silver")
label3.pack()

button1 = tk.Button(window, bg="red", text="Button1")
button1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

button2 = tk.Button(window, bg="red", text="Button2")
button2.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

window.mainloop()