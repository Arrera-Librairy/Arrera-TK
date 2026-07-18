import customtkinter as ctk
from tkinter import StringVar
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aOptionMenu(placement_Tool_Kit_internet, ctk.CTkOptionMenu):
    def __init__(self, master, value: list, police_size: int = 15, bg: str = "", fg: str = "", width: int = 200,
                 **kwargs):
        self.__var = StringVar()

        super().__init__(master, values=value, variable=self.__var,width=width, **kwargs)

        if bg != "":
            self.configure(fg_color=bg)

        if fg != "":
            self.configure(text_color=fg)

        self.configure(font=("Roboto", police_size, "bold"))

        self.__var.set(value[0])

    def getValue(self):
        return self.__var.get()

    def changeColor(self, bg: str = "", fg: str = ""):
        if bg != "":
            self.configure(fg_color=bg)

        if fg != "":
            self.configure(text_color=fg)

    def changePolice(self, font: tuple[str, int, str] = ("Roboto", 15, "bold")):
        self.configure(font=font)

    def set_text(self, text: str):
        self.__var.set(text)
