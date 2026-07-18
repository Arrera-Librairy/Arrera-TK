import customtkinter as ctk
import platform
import os
from tkinter import PhotoImage
from .utils import resource_path

class aTopLevel(ctk.CTkToplevel):
    def __init__(self, title: str = "Arrera TopLevel", width: int = 400, height: int = 300, resizable: bool = False,
                 icon: str = "", **kwargs):
        super().__init__(**kwargs)

        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable, resizable)

        if icon != "":
            icon = resource_path(icon)
            if platform.system() == "Windows" and os.path.splitext(icon)[1].lower() == '.ico':
                self.iconbitmap(icon)
            elif os.path.splitext(icon)[1].lower() == '.png':
                self.iconphoto(True, PhotoImage(file=icon))
