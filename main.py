import tkinter as tk
from tkinter import ttk
import requests, json
from bs4 import BeautifulSoup as bs
from tkinter import *


window = Tk()
window.title("Currency Converter")
window.minsize(width=300,height=300)



first_label = Label(text="Please choose the first currency and input the amount: ")
first_label.pack()


combobox1 = ttk.Combobox(values=["USD", "EUR", "GBP", "AUD ", "DKK", "SEK", "CHF", "JPY", "CAD"])
combobox1.pack(pady=10)

amount_entry = Entry()
amount_entry.pack()

second_label = Label(text="Please choose currency that you would like to convert to: ")
second_label.pack()


combobox2 = ttk.Combobox(values=["USD", "EUR", "GBP", "AUD ", "DKK", "SEK", "CHF", "JPY", "CAD"])
combobox2.pack(pady=10)

result= Label(window, text='Result  :')



class CurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']

def clear():
    combobox1.delete(0, END)
    combobox2.delete(0, END)
    amount_entry.delete(0, END)

def convert():
    source_currency = combobox1.get()
    target_currency = combobox2.get()
    amount_str = amount_entry.get()
    amount = float(amount_str)

    response = requests.get(
            f"https://www.x-rates.com/calculator/?from={source_currency}&to={target_currency}&amount=1")
    soup = bs(response.text, "html.parser")

    text1 = soup.find(class_="ccOutputTrail").previous_sibling
    text2 = soup.find(class_="ccOutputTrail").get_text(strip=True)
    rate = "{}{}".format(text1, text2)
    result_value = amount * float(rate)

    res.config(text=result_value, font='Helvetica 10 bold')

res = Label(window, text='', font='Helvetica 10 bold')
res.pack()

button = tk.Button(window, text='Convert', command=convert)
button.pack()

button2 = tk.Button(window, text='Clear', command=clear)
button2.pack()

window.mainloop()