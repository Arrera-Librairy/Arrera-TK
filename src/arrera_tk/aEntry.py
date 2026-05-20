import customtkinter as ctk
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aEntry(placement_Tool_Kit_internet, ctk.CTkEntry):
    def __init__(self, master, police_size: int = 15, width: int = 20, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("Roboto", police_size, "bold"))
        self.configure(width=width)
