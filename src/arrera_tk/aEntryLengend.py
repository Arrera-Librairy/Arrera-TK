import customtkinter as ctk
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet
from .aLabel import aLabel
from .aEntry import aEntry

class aEntryLengend(placement_Tool_Kit_internet, ctk.CTkFrame):
    def __init__(self, master, text: str = "Arrera Entry Legend", bg: str = "", fg: str = "", police_size: int = 15,
                 width: int = 200, gridUsed: bool = False):
        super().__init__(master)
        text = text + ":  "
        self.__label = aLabel(self, text=text, font=("Roboto", police_size, "bold"))


        if bg == "":
            bg = master.cget("fg_color")

        self.configure(fg_color=bg)
        self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

        self.__entry = aEntry(self, police_size=police_size, width=width)

        if gridUsed:
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=0)
            self.__label.grid(row=0, column=0, sticky="w", padx=(8, 6), pady=6)
            self.__entry.grid(row=0, column=1, sticky="ew", padx=(6, 8), pady=6)
        else:
            self.__label.pack(side="left")
            self.__entry.pack(side="right")

    def getEntry(self):
        return self.__entry

    def changeColorLabel(self, bg: str = "", fg: str = ""):
        if bg != "":
            self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

    def changeTextLabel(self, text: str):
        self.__label.configure(text=text)

    def changePoliceLabel(self, font: tuple[str, int, str] = ("Roboto", 15, "bold")):
        self.__label.configure(font=font)
