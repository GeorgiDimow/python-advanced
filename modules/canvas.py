from tkinter import Tk, Canvas


def create_root():
    root = Tk()

    root.title("GUI Shop")
    root.resizable(False, False)
    root.geometry("700x600")
    root['background'] = '#856ff8'

    return root


def crate_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)
    frame.configure(background='#F5EDBE')
    return frame


root = create_root()
frame = crate_frame()