import customtkinter as ctk
from tkinter import *
from PIL import Image
import webbrowser as wb
import platform
import os
import sys

from customtkinter import CTkCanvas

VERSIONARRERATK = "2.0.0"

# Fonction pour gerer les resource sur mac os
def resource_path(relative_path):
    if platform.system() == "Darwin":
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
    else:
        return relative_path

# Widget

class aLabel(ctk.CTkLabel):
    def __init__(self, master, text: str = "Arrera Label", **kwargs):
        super().__init__(master, text=text, **kwargs)

class aButton(ctk.CTkButton):
    def __init__(self, master, text: str = "Arrera Button", width: int = 140, height: int = 40, command=None, **kwargs):
        super().__init__(master, text=text, width=width, height=height, command=command, **kwargs)

class aCheckBox(ctk.CTkCheckBox):
    def __init__(self,master,boolean_value:bool):
        if boolean_value:
            self.__bVar = BooleanVar(master,value=True)
        else :
            self.__bVar = BooleanVar(master,value=True)
        super().__init__(master,variable=self.__bVar,text="Arrera CheckBox")

    def getBooleanVar(self):
        return self.__bVar

    def setFalse(self):
        self.__bVar.set(False)

    def setTrue(self):
        self.__bVar.set(True)

class aRadioButton(ctk.CTkRadioButton):
    def __init__(self, master, text: str = "Arrera RadioButton", variable=None, value=0, command=None, **kwargs):
        super().__init__(master, text=text, variable=variable, value=value, command=command, **kwargs)

class aEntry(ctk.CTkEntry):
    def __init__(self,master,police_size:int=15,width:int=20):
        super().__init__(master)
        self.configure(font=("Roboto",police_size,"bold"))
        self.configure(width=width)

class aText(ctk.CTkTextbox):
    def __init__(self,master,police_size:int=15,center:bool=False):
        super().__init__(master)
        self.configure(font=("Roboto",police_size,"normal"))

        if center:
            self._textbox.tag_configure("center", justify="center")
            self._textbox.tag_add("center", "0.0", "end")

class aTextScrollable(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(border_width=0)

        self.__textbox = ctk.CTkTextbox(self, wrap="word", state="disabled")
        scrollbar = ctk.CTkScrollbar(self, command=self.__textbox.yview)
        self.__textbox.configure(yscrollcommand=scrollbar.set)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.__textbox.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)
        scrollbar.grid(row=0, column=1, sticky="ns", padx=(0, 10), pady=10)

    def getTextBox(self):
        return self.__textbox

    def enableTextBox(self):
        self.__textbox.configure(state="normal")
        self.__textbox.focus()

    def disableTextBox(self):
        self.__textbox.configure(state="disabled")

class aEntryLengend(ctk.CTkFrame):
    def __init__(self,master,text:str="Arrera Entry Legend",bg:str="",fg:str="",police_size:int=15,width:int=200,gridUsed:bool=False):
        super().__init__(master)
        text = text + ":  "
        self.__label = aLabel(self,text=text,font=("Roboto",police_size,"bold"))

        if bg != "":
            self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

        self.__entry = aEntry(self,police_size=police_size,width=width)

        if gridUsed:
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=0)
            self.__label.grid(row=0, column=0, sticky="w",  padx=(8, 6), pady=6)
            self.__entry.grid(row=0, column=1, sticky="ew", padx=(6, 8), pady=6)
        else :
            self.__label.pack(side="left")
            self.__entry.pack(side="right")

    def getEntry(self):
        return self.__entry

    def changeColorLabel(self,bg:str="",fg:str=""):
        if bg != "":
            self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

    def changeTextLabel(self,text:str):
        self.__label.configure(text=text)

    def changePoliceLabel(self,font:(str,int,str)=("Roboto",15,"bold")):
        self.__label.configure(font=font)

class aOptionMenu(ctk.CTkOptionMenu):
    def __init__(self,master,value:list,police_size:int=15,bg:str="",fg:str="",width:int=200):
        self.__var = StringVar()

        super().__init__(master,values=value,variable=self.__var)

        if bg != "":
            self.configure(fg_color=bg)

        if fg != "":
            self.configure(text_color=fg)

        self.configure(font=("Roboto",police_size,"bold"))

        self.__var.set(value[0])

    def getValue(self):
        return self.__var.get()

    def changeColor(self,bg:str="",fg:str=""):
        if bg != "":
            self.configure(fg_color=bg)

        if fg != "":
            self.configure(text_color=fg)

    def changePolice(self,font:(str,int,str)=("Roboto",15,"bold")):
        self.configure(font=font)

class aOptionMenuLengend(ctk.CTkFrame):
    def __init__(self,master,values:list,text:str="Arrera OptionMenu Legend",bg:str="",fg:str="",police_size:int=15,gridUsed:bool=False):
        super().__init__(master)
        text = text + ":  "
        self.__label = aLabel(self,text=text,font=("Roboto",police_size,"bold"))

        if bg != "":
            self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

        self.__optionMenu = aOptionMenu(self,value=values,police_size=police_size,bg=bg,fg=fg)

        if gridUsed:
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=0)
            self.__label.grid(row=0, column=0, sticky="w",  padx=(8, 6), pady=6)
            self.__optionMenu.grid(row=0, column=1, sticky="ew", padx=(6, 8), pady=6)
        else :
            self.__label.pack(side="left")
            self.__optionMenu.pack(side="right")

    def getOptionMenu(self):
        return self.__optionMenu

    def getValue(self):
        return self.__optionMenu.getValue()

    def changeColorLabel(self,bg:str="",fg:str=""):
        if bg != "":
            self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

    def changeTextLabel(self,text:str):
        self.__label.configure(text=text)

    def changePoliceLabel(self,font:(str,int,str)=("Roboto",15,"bold")):
        self.__label.configure(font=font)

class aHourPickers(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        hours   = [f"{h:02d}" for h in range(24)]
        minutes = [f"{m:02d}" for m in range(60)]

        self.__hour = aOptionMenu(self,value=hours,width=10)
        self.__minute = aOptionMenu(self,value=minutes,width=10)

        label = aLabel(self,text=" : ",font=("Roboto",20,"bold"))

        self.__hour.pack(side="left")
        label.pack(side="left")
        self.__minute.pack(side="left")

    def getValueHour(self):
        return self.__hour.getValue()

    def getValueMinute(self):
        return self.__minute.getValue()

class aSwicht(ctk.CTkSwitch):
    def __init__(self,master,text="Arrera Button Swicht",default_value:bool=False,**kwargs):
        self.__var = BooleanVar(value=default_value)
        super().__init__(master,text=text,variable=self.__var,onvalue=True,offvalue=False,**kwargs)
        self.configure(font=("Roboto",15,"bold"))

    def setOn(self):
        self.__var.set(True)

    def setOff(self):
        self.__var.set(False)

    def getValue(self):
        return self.__var.get()

    def change_text(self,text=""):
        if text != "":
            self.configure(text=text)


# Frame / Canvas

class aFrame(ctk.CTkFrame):
    def __init__(self, master,corner_radius: int = 20, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=corner_radius)

class aScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,corner_radius: int = 20, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=corner_radius)

class aCanvas(ctk.CTkCanvas):
    def __init__(self,master):
        super().__init__(master)

class aBackgroundImage(ctk.CTkFrame):
    def __init__(self,master,background_light:str,background_dark:str="",height:int = 600,width:int = 800):
        if background_dark != "":
            background = ctk.CTkImage(light_image=Image.open(resource_path(background_light)),
                                      dark_image=Image.open(resource_path(background_light)),
                                      size=(width, height))
        else :
            background = ctk.CTkImage(light_image=Image.open(resource_path(background_light)),
                                      dark_image=Image.open(resource_path(background_dark)),
                                      size=(width, height))
        self.__size = (width,height)
        super().__init__(master)
        self.configure(width=width,height=height)
        self.configure(border_width=0)

        self.__label = aLabel(self,text="",image=background)
        self.__label.place(relx=0.5, rely=0.5, anchor='center')

    def change_background(self,background_light:str,background_dark:str=""):
        if background_dark != "":
            background = ctk.CTkImage(light_image=Image.open(resource_path(background_light)),
                                      dark_image=Image.open(resource_path(background_light)),
                                      size=self.__size)
        else :
            background = ctk.CTkImage(light_image=Image.open(resource_path(background_light)),
                                      dark_image=Image.open(resource_path(background_dark)),
                                      size=self.__size)

        self.__label.configure(image=background)
        self.update()

# Fenetre

class aTk(ctk.CTk):
    def __init__(self, title: str = "ArreraTK", width: int = 800, height: int = 600, resizable: bool = False, icon: str = "",theme_file:str="theme/theme_material3.json"):
        super().__init__()
        try :
            ctk.set_default_color_theme(resource_path(theme_file))
        except :
            ctk.set_default_color_theme("dark-blue")

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
    def __init__(self, title: str = "Arrera TopLevel", width: int = 400, height: int = 300, resizable: bool = False, icon: str = ""):
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

class windows_about(ctk.CTkToplevel):
    def __init__(self,nameSoft:str,iconFile:str,version:str,copyright:str,linkSource:str,linkWeb:str):
        super().__init__()
        self.title("A propos : "+nameSoft)
        self.maxsize(400,300)
        self.minsize(400,300)


        icon = ctk.CTkImage(light_image=Image.open(resource_path(iconFile)), size=(100, 100))
        mainFrame = aFrame(self,width=400,height=250,border_width=0,corner_radius=0)
        frameBTN = aFrame(self,width=400,height=50,border_width=0,corner_radius=0)
        frameLabel = aFrame(self,border_width=0,corner_radius=0)

        labelIcon = aLabel(mainFrame,image=icon,text="")
        labelSoft = aLabel(frameLabel,text=nameSoft+" version "+version,font=("Roboto",20))
        labelVersion = aLabel(frameLabel,text="Arrera TK version "+VERSIONARRERATK,font=("Roboto",13))
        labelCopy = aLabel(mainFrame,text=copyright,font=("Roboto",13))

        btnLinkSource = aButton(frameBTN,text="Source code",command= lambda :  wb.open(linkSource),
                                      font=("Roboto", 13,"bold"))
        btnLinkWeb = aButton(frameBTN,text="Web site",command= lambda :  wb.open(linkWeb),
                                   font=("Roboto", 13,"bold"))

        labelIcon.place(relx=0.5, rely=0.0, anchor="n")
        labelSoft.pack()
        labelVersion.pack()
        labelCopy.place(relx=0.5, rely=1.0, anchor="s")

        frameLabel.place(relx=0.5, rely=0.5, anchor="center")
        mainFrame.pack(side="top")
        frameBTN.pack(side ="bottom")


        btnLinkSource.place(relx=1, rely=1, anchor='se')
        btnLinkWeb.place(relx=0, rely=1, anchor='sw')
