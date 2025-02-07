#!/usr/bin/python3.12
import tkinter as tk

def label(text, fg, bg, font):
    return tk.Label(text=text, fg=fg, bg=bg, font=font, bd=0, padx=0, pady=0)

def button(text, fg, bg, activefg, activebg, font):
    return tk.Button(text=text, fg=fg, bg=bg, activeforeground=activefg, activebackground=activebg, font=font, relief="SOLID", bd=0, padx=0, pady=0)

