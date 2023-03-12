from json import loads, dump
from tkinter import Button, Entry

from buying_page import display_products
from canvas import root, frame
from helpers import clean_screen
from menu import menu_page


def get_users_data():
    info_data = []

    with open("db/users_information.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def render_entry():
    register_btn = Button(
        root,
        text="Register",
        font=("Courier New", 10),
        bg="#28A737",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=register,
    )

    login_btn = Button(
        root,
        text="Login",
        font=("Courier New", 10),
        bg="#009FE3",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 260, window=register_btn)
    frame.create_window(350, 320, window=login_btn)


def register():
    clean_screen()

    frame.create_text(90, 50, text="First name:", font=("Courier New", 10))
    frame.create_text(90, 100, text="Last name:", font=("Courier New", 10))
    frame.create_text(90, 150, text="Username:", font=("Courier New", 10))
    frame.create_text(90, 200, text="Password:", font=("Courier New", 10))

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    registration_btn = Button(
        root,
        text="Register",
        font=("Courier New", 10),
        bg="#28A737",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=registration,
    )

    frame.create_window(350, 300, window=registration_btn)


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:", font=("Courier New", 10))
    frame.create_text(100, 100, text="Password:", font=("Courier New", 10))

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    login_btn = Button(
        root,
        text="Login",
        font=("Courier New", 10),
        bg="#009FE3",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=logging
    )

    frame.create_window(350, 200, window=login_btn)


def registration():
    info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get(),
    }

    if check_registration(info_dict):
        with open("db/users_information.txt", 'a') as users_file:
            dump(info_dict, users_file)
            users_file.writelines("\n")
            menu_page()


def check_registration(info):
    for el in info.values():
        if not el.split():
            frame.create_text(
                350,
                350,
                text="We are missing some information",
                font=("Courier New", 9),
                fill="red",
                tag="error"
            )

            return False

    frame.delete("error")

    info_data = get_users_data()

    for record in info_data:
        if record["username"] == info["username"]:
            frame.create_text(
                350,
                350,
                text="User with this username exists!",
                fill="red",
                tag="error",
                font=("Courier New", 9),
            )

            return False

    frame.delete("error")

    return True


def logging():
    if check_logging():
        menu_page()
    else:
        frame.create_text(160, 200, text="Invalid username or password!", fill="red", font=("Courier New", 9),)


def check_logging():
    info_data = get_users_data()
    user_username = username_box.get()
    user_password = password_box.get()

    for i in range(len(info_data)):
        username = info_data[i]["username"]
        password = info_data[i]["password"]

        if username == user_username and password == user_password:
            return True

    frame.delete("error")

    return False


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")
