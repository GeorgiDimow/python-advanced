from json import load, dump
from tkinter import Button, ttk

from canvas import frame, root
from helpers import clean_screen


def order_page(item_name, item_image):
    clean_screen()
    order_interface(item_name, item_image)


def order_interface(item_name, item_img):
    global info

    with open("db/products_data.json", 'r') as stock:
        info = load(stock)

    frame.create_text(350, 50, text=item_name, font=("Comic Sans MS", 15))
    frame.create_image(350, 150, image=item_img)

    values = ["S", "M", "L"]

    combo = ttk.Combobox(root, values=values)
    frame.create_window(350, 250, window=combo)

    buy_btn = Button(
        root,
        text="Buy",
        font=("Montserrat Medium 500", 12),
        bg="red",
        fg="white",
        width=5,
        command=lambda x=item_name, y=combo : buy_prod(x, y, item_img)
    )
    sizes_text = ''

    for size in values:
        sizes_text += f"{size}: {info[item_name]['quantity'][size]} "

    frame.create_text(350, 350, text=sizes_text, font=("Montserrat Medium 500", 12))
    frame.create_window(350, 300, window=buy_btn)


def buy_prod(prod, combo, img):
    if len(combo.get()) != 0:
        size = combo.get()
        if info[prod]['quantity'][size] > 0:

            info[prod]['quantity'][size] -= 1
            with open('db/products_data.json', 'w') as stock:
                dump(info, stock)
            order_page(prod, img)

        else:
            frame.create_text(350, 400, text=f"{size} size out of stock", fill="red")

    else:
        frame.create_text(350, 400, text="No selected size", fill="red")



