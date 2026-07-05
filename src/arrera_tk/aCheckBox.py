import customtkinter as ctk
from tkinter import BooleanVar
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aCheckBox(placement_Tool_Kit_internet, ctk.CTkCheckBox):
    def __init__(self, master, boolean_value: bool, **kwargs):
        if boolean_value:
            self.__bVar = BooleanVar(master, value=True)
        else:
            self.__bVar = BooleanVar(master, value=False)

        text_value = kwargs.pop('text', "Arrera CheckBox")
        super().__init__(master, variable=self.__bVar, text=text_value, **kwargs)

    def getBooleanVar(self):
        return self.__bVar

    def setFalse(self):
        self.__bVar.set(False)

    def setTrue(self):
        self.__bVar.set(True)
