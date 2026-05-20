import customtkinter as ctk
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aText(placement_Tool_Kit_internet, ctk.CTkTextbox):
    def __init__(self, master, police_size: int = 15, center: bool = False, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("Roboto", police_size, "normal"))

        if center:
            self._textbox.tag_configure("center", justify="center")
            self._textbox.tag_add("center", "0.0", "end")

    def disable_textbox(self):
        self.configure(state="disabled")

    def enable_textbox(self):
        self.configure(state="normal")
        self.focus()

    def insert_text(self, text: str):
        self.configure(state="normal")
        self.insert("1.0", text)
        self.configure(state="disabled")

    def centre_text(self):
        self._textbox.tag_configure("center", justify="center")
