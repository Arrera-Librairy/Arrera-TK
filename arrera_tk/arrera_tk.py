import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

class CArreraTK :
    def __init__(self):
        self.__mode = 0
        self.__windowsColor = ""
        self.__textColor = ""

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


    def createImage(self, pathLight: str, pathDark: str = "none", tailleX: int = 250, tailleY: int = 250):
        if (self.__mode == 0):
            if (pathDark != "none"):
                image = ctk.CTkImage(
                    light_image=Image.open(pathLight),
                    dark_image=Image.open(pathDark),
                    size=(tailleX, tailleY))
                return image
            else :
                image = ctk.CTkImage(
                    light_image=Image.open(pathLight),
                    size=(tailleX, tailleY))
                return image
        else :
            if (pathDark != "none"):
                imageLight = PhotoImage(file=pathLight)
                imageDark = PhotoImage(file=pathDark)
                return [imageLight, imageDark]
            else :
                imageLight = PhotoImage(file=pathLight)
                return imageLight

    def createLabel(self, screen, text: str = "", image = None,bg : str = "", fg : str = ""):
        if (self.__mode == 0):
            label = ctk.CTkLabel(screen)
            if (text != ""):
                label.configure(text=text)
            if (image != None):
                label.configure(image=image)
            if (bg != ""):
                label.configure(bg_color=bg)
            if (fg != ""):
                label.configure(fg_color=fg)
        else :
            label = Label(screen)
            if (text != ""):
                label.configure(text=text)
            if (image != None):
                label.configure(image=image)
            if (bg != ""):
                label.configure(bg=bg)
            if (fg != ""):
                label.configure(fg=fg)
        return label

    def createButton(self, screen, text: str = "", image = None,bg : str = "", fg : str = "",command = None):
        if (self.__mode == 0):
            btn = (ctk.CTkButton(screen))
            if (text != ""):
                btn.configure(text=text)
            if (image != None):
                btn.configure(image=image)
            if (bg != ""):
                btn.configure(bg_color=bg)
            if (fg != ""):
                btn.configure(fg_color=fg)
            if (command != None):
                btn.configure(command=command)
        else :
            btn = Button(screen)
            if (text != ""):
                btn.configure(text=text)
            if (image != None):
                btn.configure(image=image)
            if (bg != ""):
                btn.configure(bg=bg)
            if (fg != ""):
                btn.configure(fg=fg)
            if (command != None):
                btn.configure(command=command)
        return btn

    def createEntry(self, screen, bg : str = "", fg : str = ""):
        if (self.__mode == 0):
            entry = ctk.CTkEntry(screen)
            if (bg != ""):
                entry.configure(bg_color=bg)
            if (fg != ""):
                entry.configure(fg_color=fg)
        else :
            entry = Entry(screen)
            if (bg != ""):
                entry.configure(bg=bg)
            if (fg != ""):
                entry.configure(fg=fg)
        return entry

    def createText(self, screen, bg : str = "", fg : str = ""):
        text = Text(screen)
        if (bg != ""):
            text.configure(bg=bg)
        if (fg != ""):
            text.configure(fg=fg)

        return text