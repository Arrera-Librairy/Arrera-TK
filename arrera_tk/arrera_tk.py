import customtkinter as ctk
from tkinter import *
import platform
import os
import sys

# Fonction pour gerer les resource sur mac os
def resource_path(relative_path):
    if platform.system() == "Darwin":
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
    else:
        return relative_path

class aTk(ctk.CTk):
    def __init__(self, title: str = "ArreraTK", width: int = 800, height: int = 600, resizable: bool = False, icon: str = "",theme_file:str="theme/theme_material3.json"):
        super().__init__()
        try :
            ctk.set_default_color_theme(resource_path(theme_file))
        except :
            ctk.set_default_color_theme("dark-blue")

        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable, resizable)
        
        if icon != "":
            icon = resource_path(icon)
            if platform.system() == "Windows":
                if os.path.splitext(icon)[1].lower() == '.ico' :
                    self.iconbitmap(icon)
            elif os.path.splitext(icon)[1].lower() == '.png' :
                self.iconphoto(True, PhotoImage(file=icon))

class aTopLevel(ctk.CTkToplevel):
    def __init__(self, title: str = "Arrera TopLevel", width: int = 400, height: int = 300, resizable: bool = False, icon: str = ""):
        super().__init__()
        
        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable, resizable)

        if icon != "":
            icon = resource_path(icon)
            if platform.system() == "Windows":
                if os.path.splitext(icon)[1].lower() == '.ico' :
                    self.iconbitmap(icon)
            elif os.path.splitext(icon)[1].lower() == '.png' :
                self.iconphoto(True, PhotoImage(file=icon))

class aLabel(ctk.CTkLabel):
    def __init__(self, master, text: str = "Arrera Label", **kwargs):
        super().__init__(master, text=text, **kwargs)

class aButton(ctk.CTkButton):
    def __init__(self, master, text: str = "Arrera Button", width: int = 140, height: int = 40, command=None, **kwargs):
        super().__init__(master, text=text, width=width, height=height, command=command, **kwargs)

class aFrame(ctk.CTkFrame):
    def __init__(self, master,corner_radius: int = 20, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=corner_radius)