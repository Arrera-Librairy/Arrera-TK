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
    def __init__(self,title: str = "ArreraTK",width: int = 800, height: int = 600, resizable: bool = False,icon: str = ""):
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

class aTopLevel(ctk.CTkToplevel):
    def __init__(self,title: str = "Arrera TopLevel",width: int = 400, height: int = 300, resizable: bool = False,icon: str = ""):
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