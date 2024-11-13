from email.policy import default

import customtkinter as ctk
from tkinter import *

class CArreraTK :
    def __init__(self):
        self.__mode = 0

    def aTK(self, mode: int = 0, width: int = 800, height: int = 600,title: str = "ArreraTK", resizable: bool = False, bg: str = "", fg: str = "", icon: str = ""):
        """
        :param mode: 1 for Tkinter, 0 for customtkinter
        :param mainWindow: True for main window, False for Toplevel
        :param width: width of the window
        :param height: height of the window
        :param title: title of the window
        :param resizable: True for resizable, False for not resizable
        :param bg:  background color
        :param fg:  text color
        :param icon: icon of the window (ico file)
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
        self.__mode = mode
        if mode == 0:
            self.__root = ctk.CTk()
        else:
            self.__root = Tk()
        if icon != "":
            self.__root.iconbitmap(icon)
        self.__root.geometry(f"{width}x{height}")
        self.__root.title(title)
        self.__root.resizable(resizable, resizable)
        if bg == "":
            self.__root.configure(bg=defaultColor)
            self.__windowsColor = defaultColor
            self.__textColor = defaultTextColor
        else:
            self.__root.configure(bg=bg)
            self.__windowsColor = bg
            self.__textColor = fg

        return self.__root

    def aTopLevel(self, mode: int = 0, width: int = 800, height: int = 600,title: str = "ArreraTK", resizable: bool = False, bg: str = "", fg: str = "", icon: str = ""):
        """
        :param mode: 1 for Tkinter, 0 for customtkinter
        :param mainWindow: True for main window, False for Toplevel
        :param width: width of the window
        :param height: height of the window
        :param title: title of the window
        :param resizable: True for resizable, False for not resizable
        :param bg:  background color
        :param fg:  text color
        :param icon: icon of the window (ico file)
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
        self.__mode = mode
        if mode == 0:
            self.__root = ctk.CTkToplevel()
        else:
            self.__root = Toplevel()
        if icon != "":
            self.__root.iconbitmap(icon)
        self.__root.geometry(f"{width}x{height}")
        self.__root.title(title)
        self.__root.resizable(resizable, resizable)
        if bg == "":
            self.__root.configure(bg=defaultColor)
            self.__windowsColor = defaultColor
            self.__textColor = defaultTextColor
        else:
            self.__root.configure(bg=bg)
            self.__windowsColor = bg
            self.__textColor = fg

        return self.__root

    def view(self):
        self.__root.mainloop()

    def title(self, title: str):
        self.__root.title(title)

    def setGeometry(self, width: int, height: int):
        self.__root.geometry(f"{width}x{height}")

    def setResizable(self, resizable: bool):
        self.__root.resizable(resizable, resizable)

    def setColor(self, bg: str, fg: str):
        self.__root.configure(bg=bg)
        self.__windowsColor = bg
        self.__textColor = fg
