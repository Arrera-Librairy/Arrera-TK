import customtkinter as ctk
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet
from .aOptionMenu import aOptionMenu
from .aLabel import aLabel

class aHourPickers(placement_Tool_Kit_internet, ctk.CTkFrame):
    def __init__(self, master,minute_pickers:bool = False, **kwargs):
        super().__init__(master,fg_color=master.cget("fg_color"),**kwargs)

        if not minute_pickers:
            hours = [f"{h:02d}" for h in range(24)]
        else :
            hours = [f"{h:02d}" for h in range(60)]

        minutes = [f"{m:02d}" for m in range(60)]

        self.__hour = aOptionMenu(self, value=hours, width=10)
        self.__minute = aOptionMenu(self, value=minutes, width=10)

        label = aLabel(self, text=" : ", font=("Roboto", 20, "bold"))

        self.__hour.pack(side="left")
        label.pack(side="left")
        self.__minute.pack(side="left")

    def getValueHour(self):
        return self.__hour.getValue()

    def getValueMinute(self):
        return self.__minute.getValue()

    def setValueMinute(self, minute:str):
        self.__minute.set(minute)

    def setValueHour(self,hour:str):
        self.__hour.set(hour)
