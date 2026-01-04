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

class ATheme:
    def __init__(self):
        # Material 3 Expressive Colors (Light, Dark)
        self.primary = ("#6750A4", "#D0BCFF")
        self.on_primary = ("#FFFFFF", "#381E72")
        self.primary_container = ("#EADDFF", "#4F378B")
        self.on_primary_container = ("#21005D", "#EADDFF")
        
        self.secondary = ("#625B71", "#CCC2DC")
        self.on_secondary = ("#FFFFFF", "#332D41")
        self.secondary_container = ("#E8DEF8", "#4A4458")
        self.on_secondary_container = ("#1D192B", "#E8DEF8")
        
        self.tertiary = ("#7D5260", "#EFB8C8")
        self.on_tertiary = ("#FFFFFF", "#492532")
        self.tertiary_container = ("#FFD8E4", "#633B48")
        self.on_tertiary_container = ("#31111D", "#FFD8E4")
        
        self.error = ("#B3261E", "#F2B8B5")
        self.on_error = ("#FFFFFF", "#601410")
        
        self.background = ("#FFFBFE", "#1C1B1F")
        self.on_background = ("#1C1B1F", "#E6E1E5")
        
        self.surface = ("#FFFBFE", "#1C1B1F")
        self.on_surface = ("#1C1B1F", "#E6E1E5")
        
        # Shapes
        self.shape_small = 4
        self.shape_medium = 12
        self.shape_large = 16
        self.shape_extra_large = 28
        
        # Typography
        self.font_family = "Roboto"

class aTk(ctk.CTk):
    def __init__(self, title: str = "ArreraTK", width: int = 800, height: int = 600, resizable: bool = False, icon: str = "", theme: ATheme = ATheme()):
        super().__init__()
        self.theme = theme if theme else ATheme()
        
        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable, resizable)
        self.configure(fg_color=self.theme.background)
        
        if icon != "":
            icon = resource_path(icon)
            if platform.system() == "Windows":
                if os.path.splitext(icon)[1].lower() == '.ico' :
                    self.iconbitmap(icon)
            elif os.path.splitext(icon)[1].lower() == '.png' :
                self.iconphoto(True, PhotoImage(file=icon))

class aTopLevel(ctk.CTkToplevel):
    def __init__(self, title: str = "Arrera TopLevel", width: int = 400, height: int = 300, resizable: bool = False, icon: str = "", theme: ATheme = ATheme()):
        super().__init__()
        self.theme = theme if theme else ATheme()
        
        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable, resizable)
        self.configure(fg_color=self.theme.background)

        if icon != "":
            icon = resource_path(icon)
            if platform.system() == "Windows":
                if os.path.splitext(icon)[1].lower() == '.ico' :
                    self.iconbitmap(icon)
            elif os.path.splitext(icon)[1].lower() == '.png' :
                self.iconphoto(True, PhotoImage(file=icon))

class aLabel(ctk.CTkLabel):
    def __init(self):
        super().__init__()


class aButton(ctk.CTkButton):
    def __init__(self, master, text: str = "Arrera Button", width: int = 140, height: int = 40, command=None, theme: ATheme = None, **kwargs):
        self.theme = theme if theme else ATheme()

        super().__init__(master, text=text, width=width, height=height, command=command, **kwargs)
        
        self.configure(
            fg_color=self.theme.primary,
            text_color=self.theme.on_primary,
            corner_radius=self.theme.shape_extra_large,
            font=(self.theme.font_family, 14, "bold")
        )