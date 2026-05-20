import customtkinter as ctk
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aButton(placement_Tool_Kit_internet, ctk.CTkButton):
    def __init__(self, master, text: str = "Arrera Button", width: int = 140, height: int = 40, command=None,
                 size: int = 0, dark_color: str = "", light_color: str = "", light_text_color: str = "",
                 dark_text_color: str = "", **kwargs):
        super().__init__(master, text=text, width=width, height=height, command=command, **kwargs)
        if size != 0:
            self.configure(font=("Roboto", size, "bold"))

        if dark_color != "" and light_color != "":
            self.configure(fg_color=(light_color, dark_color))

        if dark_text_color != "" and light_text_color != "":
            self.configure(text_color=(light_text_color, dark_text_color))
