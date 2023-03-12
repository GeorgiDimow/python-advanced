from json import load, dump
from tkinter import Button, Label, Menu

from PIL import Image, ImageTk

from canvas import frame, root
from helpers import clean_screen
from buying_page import display_products


def exit():
    root.destroy()


def menu_page():
    clean_screen()

    menu_bar = Menu()

    file_menu = Menu(menu_bar, tearoff=False)
    man_menu = Menu(menu_bar, tearoff=False)
    woman_menu = Menu(menu_bar, tearoff=False)
    kids_menu = Menu(menu_bar, tearoff=False)

    menu_bar.add_cascade(label="Exit", underline=0, menu=file_menu)
    menu_bar.add_cascade(label="Man", underline=0, menu=man_menu)
    menu_bar.add_cascade(label="Woman", underline=0, menu=woman_menu)
    menu_bar.add_cascade(label="Kids", underline=0, menu=kids_menu)

    file_menu.add_command(label="Quit", underline=1, command=exit, accelerator="Ctrl+Q")

    man_menu.add_command(label="Shoes", underline=1, command=display_products)
    woman_menu.add_command(label="Shoes", underline=1, command=display_products)
    kids_menu.add_command(label="Shoes", underline=1, command=display_products)

    man_menu.add_command(label="Jeans", underline=1, command=display_products)
    woman_menu.add_command(label="Jeans", underline=1, command=display_products)
    kids_menu.add_command(label="Jeans", underline=1, command=display_products)

    man_menu.add_command(label="Shirts", underline=1, command=display_products)
    woman_menu.add_command(label="Shirts", underline=1, command=display_products)
    kids_menu.add_command(label="Shirts", underline=1, command=display_products)

    root.config(menu=menu_bar)
    menu_bar.configure(background='blue', fg='white')

