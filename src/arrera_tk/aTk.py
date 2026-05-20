import customtkinter as ctk
import platform
import os
from tkinter import PhotoImage
from .utils import resource_path

class aTk(ctk.CTk):
    def __init__(self, title: str = "ArreraTK", width: int = 800, height: int = 600, resizable: bool = False,
                 icon: str = "", theme_file: str = "theme/theme_default.json", **kwargs):
        super().__init__(**kwargs)
        ctk.set_appearance_mode("System")
        try:
            ctk.set_default_color_theme(resource_path(theme_file))
        except Exception as e:
            print(e)
            ctk.set_default_color_theme("dark-blue")

        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable, resizable)

        if icon != "":
            icon = resource_path(icon)
            if platform.system() == "Windows":
                if os.path.splitext(icon)[1].lower() == '.ico':
                    self.iconbitmap(icon)
            elif os.path.splitext(icon)[1].lower() == '.png':
                self.iconphoto(True, PhotoImage(file=icon))
