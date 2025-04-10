import tkinter as tk

window = tk.Tk()

button = tk.Button(
    window,
    text = "QUIT",
    border=10,
    fg="red",
    bg="silver",
    activeforeground="orange",
    activebackground="silver",
    font="Times 24",
    height=3,
    width=30,
    padx=5,
    pady=5,
    relief="groove",
    command=quit
)

button.pack()

window.mainloop()