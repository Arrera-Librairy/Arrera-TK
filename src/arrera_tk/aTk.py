import customtkinter as ctk
import platform
import os
import json
import tempfile
from tkinter import PhotoImage
from .utils import resource_path
from .theme import *

dict_themes = {
            "defaut": theme_defaut,
            "blanc": theme_blanc,
            "blanc-gris": theme_blanc_gris,
            "bleu": theme_bleu,
            "bleu-blanc": theme_bleu_blanc,
            "bleu-violet": theme_bleu_violet,
            "gris": theme_gris,
            "jaune": theme_jaune,
            "orange": theme_orange,
            "rose": theme_rose,
            "rouge": theme_rouge
        }

list_theme = list(dict_themes.keys())

class aTk(ctk.CTk):
    _theme_cache = {}

    def __init__(self, title: str = "ArreraTK", width: int = 800, height: int = 600, resizable: bool = False,
                 icon: str = "", theme: str = "defaut", **kwargs):
        super().__init__(**kwargs)
        ctk.set_appearance_mode("System")
        
        self.__apply_theme(theme)

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

    @classmethod
    def __theme_dict_to_path(cls, theme_dict):
        cache_key = json.dumps(theme_dict, sort_keys=True)
        theme_cache = cls._theme_cache
        if cache_key not in theme_cache:
            fd, theme_path = tempfile.mkstemp(prefix="arrera_tk_theme_", suffix=".json")
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(theme_dict, f)
            theme_cache[cache_key] = theme_path
        return theme_cache[cache_key]

    def __apply_theme(self, theme_name: str):
        if isinstance(theme_name, dict):
            ctk.set_default_color_theme(type(self).__theme_dict_to_path(theme_name))
        elif theme_name in dict_themes:
            ctk.set_default_color_theme(type(self).__theme_dict_to_path(dict_themes[theme_name]))
        elif os.path.exists(theme_name):
             try:
                ctk.set_default_color_theme(resource_path(theme_name))
             except Exception as e:
                ctk.set_default_color_theme("dark-blue")
        else:
            ctk.set_default_color_theme(type(self).__theme_dict_to_path(theme_defaut))
