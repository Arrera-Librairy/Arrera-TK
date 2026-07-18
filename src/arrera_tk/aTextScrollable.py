import customtkinter as ctk
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aTextScrollable(placement_Tool_Kit_internet, ctk.CTkFrame):
    def __init__(self, master,police_size: int = 15):
        super().__init__(master)
        self.configure(border_width=0)

        self.__textbox = ctk.CTkTextbox(self, wrap="word", state="disabled")

        self.__textbox.configure(font=("Roboto", police_size, "normal"))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.__textbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def getTextBox(self):
        return self.__textbox

    def enableTextBox(self):
        self.__textbox.configure(state="normal")
        self.__textbox.focus()

    def disableTextBox(self):
        self.__textbox.configure(state="disabled")
