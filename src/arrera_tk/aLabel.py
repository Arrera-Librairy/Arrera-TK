import customtkinter as ctk
from customtkinter import CTkImage
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aLabel(placement_Tool_Kit_internet, ctk.CTkLabel):
    def __init__(self, master, text: str = "Arrera Label", police_size: int = 0, dark_color: str = "",
                 light_color: str = "", light_text_color: str = "", dark_text_color: str = "",image : CTkImage = None, **kwargs):
        super().__init__(master, text=text, **kwargs)
        if police_size != 0:
            self.configure(font=("Roboto", police_size, "bold"))

        if dark_color != "" and light_color != "":
            self.configure(fg_color=(light_color, dark_color))

        if dark_text_color != "" and light_text_color != "":
            self.configure(text_color=(light_text_color, dark_text_color))

        if image is not None:
            self.configure(image=image,text="")
