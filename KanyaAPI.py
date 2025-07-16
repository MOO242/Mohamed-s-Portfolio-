from shlex import quote
from tkinter import *
import requests


"""' Funcations"""


def kanye():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quoto = response.json()["quote"]
    canvas.itemconfig(Kanya_quoto, text=quoto, font=("Ariel", 20, "bold"), fill="black")


"""'' UI """ ""

window = Tk()
window.title("Kanye Quotes....")
window.config(padx=50, pady=50, background="grey")


canvas = Canvas(width=300, height=414, highlightthickness=0, background="grey")
Kanya_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=Kanya_img)
Kanya_quoto = canvas.create_text(
    150, 207, text="", width=250, font=("Ariel", 20, "bold")
)
canvas.grid(column=0, row=0)


""" Buttom"""

my_image1 = PhotoImage(file="Kanye.png")
new_buttom1 = Button(image=my_image1, highlightthickness=0, command=kanye)
new_buttom1.grid(column=0, row=2)


window.mainloop()
