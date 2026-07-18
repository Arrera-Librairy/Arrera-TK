import customtkinter as ctk
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet
from .aLabel import aLabel
from .aOptionMenu import aOptionMenu

class aOptionMenuLengend(placement_Tool_Kit_internet, ctk.CTkFrame):
    def __init__(self, master, values: list, text: str = "Arrera OptionMenu Legend", bg: str = "", fg: str = "",
                 police_size: int = 15, gridUsed: bool = False):
        super().__init__(master)
        text = text + ":  "
        self.__label = aLabel(self, text=text, font=("Roboto", police_size, "bold"))

        self.configure(fg_color=master.cget("fg_color"))

        if bg != "":
            self.__label.configure(fg_color=bg)
        else :
            self.__label.configure(fg_color=master.cget("fg_color"))

        if fg != "":
            self.__label.configure(text_color=fg)

        self.__optionMenu = aOptionMenu(self, value=values, police_size=police_size, bg=bg, fg=fg)

        if gridUsed:
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=0)
            self.__label.grid(row=0, column=0, sticky="w", padx=(8, 6), pady=6)
            self.__optionMenu.grid(row=0, column=1, sticky="ew", padx=(6, 8), pady=6)
        else:
            self.__label.pack(side="left")
            self.__optionMenu.pack(side="right")

    def getOptionMenu(self):
        return self.__optionMenu

    def getValue(self):
        return self.__optionMenu.getValue()

    def changeColorLabel(self, bg: str = "", fg: str = ""):
        if bg != "":
            self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

    def changeTextLabel(self, text: str):
        self.__label.configure(text=text)

    def set_text(self, text: str):
        self.__optionMenu.set_text(text)

    def changePoliceLabel(self, font: tuple[str, int, str] = ("Roboto", 15, "bold")):
        self.__label.configure(font=font)
