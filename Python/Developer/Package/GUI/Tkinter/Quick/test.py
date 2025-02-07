#!python
import tkinter as tk
import salah.gui.tk.tools as tk_tools

app = tk.Tk()

app.config(background="#000")
app.title("Custom App")
app.geometry("760x450")

label = tk_tools.label(text="Hello, World", fg="#000", bg="#fff", font=("0xProto Nerd Font Mono", 18, "normal"))
label.pack()

button = tk_tools.button(text="Press", fg="#000", bg="#fff", activefg="#fff", activebg="#000", font=("0xProto Nerd Font Mono", 18, "normal"))
button.place(x=10, y=10)

app.mainloop()
