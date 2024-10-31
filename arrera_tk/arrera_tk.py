from email.policy import default

import customtkinter as ctk
from tkinter import *

class CArreraTK :
    def __init__(self, mode:int=0, mainWindow:bool=True, width:int=800, height:int=600, title:str= "ArreraTK", resizable:bool=False,bg:str="",fg:str="",icon:str=""):
        """
        :param mode: 1 for Tkinter, 0 for customtkinter
        :param mainWindow: True for main window, False for Toplevel
        :param width: width of the window
        :param height: height of the window
        :param title: title of the window
        :param resizable: True for resizable, False for not resizable
        :param bg:  background color
        :param fg:  text color
        :param icon: icon of the window
        """

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        ctheme = ctk.get_appearance_mode()
        if ctheme == "Dark":
            defaultColor = ctk.ThemeManager.theme["CTk"]["fg_color"][1]
            defaultTextColor = ctk.ThemeManager.theme["CTk"]["fg_color"][0]
        else:
            defaultColor = ctk.ThemeManager.theme["CTk"]["fg_color"][0]
            defaultTextColor = ctk.ThemeManager.theme["CTk"]["fg_color"][1]
        if mode == 0:
            if mainWindow:
                self.__root = ctk.CTk()
            else :
                self.__root = ctk.CTkToplevel()
        else:
            if mainWindow:
                self.__root = Tk()
            else :
                self.__root = Toplevel()
        if icon != "":
            self.__root.iconbitmap(icon)
        self.__root.geometry(f"{width}x{height}")
        self.__root.title(title)
        self.__root.resizable(resizable,resizable)
        if bg == "":
            self.__root.configure(bg=defaultColor)
            self.__windowsColor = defaultColor
            self.__textColor = defaultTextColor
        else:
            self.__root.configure(bg=bg)
            self.__windowsColor = bg
            self.__textColor = fg

        self.__root.mainloop()
