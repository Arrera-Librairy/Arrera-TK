import customtkinter as ctk
from tkinter import BooleanVar
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aSwicht(placement_Tool_Kit_internet, ctk.CTkSwitch):
    def __init__(self, master, text="Arrera Button Swicht", default_value: bool = False, **kwargs):
        self.__var = BooleanVar(value=default_value)
        super().__init__(master, text=text, variable=self.__var, onvalue=True, offvalue=False, **kwargs)
        self.configure(font=("Roboto", 15, "bold"))

    def setOn(self):
        self.__var.set(True)

    def setOff(self):
        self.__var.set(False)

    def getValue(self):
        return self.__var.get()

    def change_text(self, text=""):
        if text != "":
            self.configure(text=text)
