import customtkinter as ctk
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aRadioButton(placement_Tool_Kit_internet, ctk.CTkRadioButton):
    def __init__(self, master, text: str = "Arrera RadioButton", variable=None, value=0, command=None, **kwargs):
        super().__init__(master, text=text, variable=variable, value=value, command=command, **kwargs)
