from json import load, dump
from tkinter import Button, Label

from PIL import Image, ImageTk

from canvas import frame, root
from helpers import clean_screen
from order_page import order_page


def display_products():
    clean_screen()
    display_t_shirts()


def display_t_shirts():
    global info
    with open("db/products_data.json", 'r') as stock:
        info = load(stock)

    x, y = 150, 100

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)

        frame.create_text(x, y + 100, text=item_name, font=("Courier New", 15))

        if item_info["quantity"]["S"] > 0 or item_info["quantity"]["L"] > 0 or item_info["quantity"]["M"] > 0:
            color = "green"

            img_label = Label(image=item_img)

            item_btn = Button(
                root,
                image=item_img,
                borderwidth=0,
                background='white',
                border=2,
                command=lambda x=item_name, y=item_img: order_page(x, y)
            )

            frame.create_window(x, y, window=item_btn)
        else:
            color = 'red'
            frame.create_text(x, y + 180, text='Out of stock', font=("Comic Sans MS", 12), fill=color)

        x += 200
        if x > 550:
            x = 150
            y += 200


images = []
info = {}