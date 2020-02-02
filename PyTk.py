import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

# Create programm
app = tk.Tk()
app.title('Searching system')
app.configure(background='#AAAAAA')

# Create text
app_name = ttk.Label(app, text='Searching application',
                     font='verdana 12 bold italic', foreground='#444444',
                     background='#AAAAAA')
app_name.grid(row=0, column=1)

search_label = ttk.Label(app, text='Search', foreground='#444444',
                         background='#AAAAAA')
search_label.grid(row=1, column=0)

# Create field for enter information
text_field = ttk.Entry(app, width=50)
text_field .grid(row=1, column=1)


search_engine = StringVar()
search_engine.set('yandex')


def search():
    if text_field.get().strip() != '':
        if search_engine.get() == 'yandex':
            webbrowser.open('https://yandex.ru/search/?text=' +
                            text_field.get())
        elif search_engine.get() == 'google':
            webbrowser.open('https://www.google.com/search?q=' +
                            text_field.get())


def searchBtn():
    search()


def enterBtn(event):
    search()


# Searching button
btn_search = ttk.Button(app, text='Find', width=10, command=searchBtn)
btn_search.grid(row=1, column=2)


text_field.bind('<Return>', enterBtn)


radio_yandex = ttk.Radiobutton(app, text='Yandex', value='yandex',
                               variable=search_engine)
radio_yandex.grid(row=2, column=1, sticky=W)

radio_google = ttk.Radiobutton(app, text='Google', value='google',
                               variable=search_engine)
radio_google.grid(row=2, column=1, sticky=E)


app.wm_attributes('-topmost', True)

text_field.focus()

# Function dont close programm
app.mainloop()
