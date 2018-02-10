import tkinter as tk

window = tk.Tk()
window.title("Little Window")
window.geometry("400x400")
lbl = tk.Label(window, text="A little window to store text")
button1 = tk.Button(text='Click me!')
button1.grid(column=0,row=0)
lbl.pack()
window.mainloop()

