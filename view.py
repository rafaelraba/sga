from tkinter import *


class View:

    def __init__(self):
        self.root = Tk()
        self.frame = Frame()

    def create_root(self, title):
        self.root.title(title)
        self.create_frame()
        self.create_labels()
        self.create_inputs()

    def create_frame(self):
        self.frame.pack(fill="both", expand=True)
        self.frame.config(width="600", height="600")

    def create_button(self, function, text):
        return Button(self.frame, text=text, command=function)

    def create_labels(self):
        Label(self.frame, text="User").grid(row=0, column=0, padx=10, pady=10)
        Label(self.frame, text="Password").grid(row=1, column=0, padx=10, pady=10)

    def create_inputs(self):
        user = Entry(self.frame)
        user.grid(row=0, column=1, padx=10, pady=10)
        password = Entry(self.frame)
        password.grid(row=1, column=1, padx=10, pady=10)
        password.config(show="*")
