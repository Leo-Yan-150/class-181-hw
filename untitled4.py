from tkinter import *
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from tkinter import ttk

root = Tk()
root.title("Stuff")
root.geometry("800x700")
root.config(bg="lavender")
language = list(LANGUAGES.values())
title = Label(root, text="Language Translator", bg="lavender", font=("times",20))
label1 = Label(root, text="output", bg="lavender", font=("times",15))
title.place(relx=0.5,rely=0.1,anchor=CENTER)
label1.place(relx=0.75,rely=0.3,anchor=CENTER)
area = Text(root, bg="orchid",font=("times",13),height=11,width=50,wrap=WORD,padx=5,pady=5,bd=0)
area.place(relx=0.75,rely=0.5,anchor=CENTER)
label11 = Label(root, text="Enter Text", bg="lavender", font=("times",15))
label11.place(relx=0.1,rely=0.3,anchor=CENTER)
area1 = Text(root, bg="orchid",font=("times",13),height=11,width=50,wrap=WORD,padx=5,pady=5,bd=0)
area1.place(relx=0.25,rely=0.5,anchor=CENTER)
boxx = ttk.Combobox(root, state = "readonly", values = language)
boxx.set("english")
boxx.place(relx=0.3,rely=0.3,anchor=CENTER)
boxxx = ttk.Combobox(root, state = "readonly", values = language)
boxxx.set("spanish")
boxxx.place(relx=0.7,rely=0.3,anchor=CENTER)
btn = Button(root, text="translate")
btn.place(relx=0.5,rely=0.7,anchor=CENTER)


root.mainloop()