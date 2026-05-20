import customtkinter as ctk
import webbrowser as wb
from PIL import Image
from .aFrame import aFrame
from .aLabel import aLabel
from .aButton import aButton
from .utils import resource_path
from . import VERSIONARRERATK

class windows_about(ctk.CTkToplevel):
    def __init__(self, nameSoft: str, iconFile: str, version: str, copyright: str, linkSource: str, linkWeb: str):
        super().__init__()
        self.title("A propos : " + nameSoft)
        self.maxsize(400, 300)
        self.minsize(400, 300)

        icon = ctk.CTkImage(light_image=Image.open(resource_path(iconFile)), size=(100, 100))
        mainFrame = aFrame(self, width=400, height=250, border_width=0, corner_radius=0)
        frameBTN = aFrame(self, width=400, height=50, border_width=0, corner_radius=0)
        frameLabel = aFrame(self, border_width=0, corner_radius=0)

        labelIcon = aLabel(mainFrame, image=icon, text="")
        labelSoft = aLabel(frameLabel, text=nameSoft + " version " + version, font=("Roboto", 20))
        labelVersion = aLabel(frameLabel, text="Arrera TK version " + VERSIONARRERATK, font=("Roboto", 13))
        labelCopy = aLabel(mainFrame, text=copyright, font=("Roboto", 13))

        btnLinkSource = aButton(frameBTN, text="Source code", command=lambda: wb.open(linkSource),
                                font=("Roboto", 13, "bold"))
        btnLinkWeb = aButton(frameBTN, text="Web site", command=lambda: wb.open(linkWeb),
                             font=("Roboto", 13, "bold"))

        labelIcon.placeTopCenter()
        labelSoft.pack()
        labelVersion.pack()
        labelCopy.placeBottomCenter()

        frameLabel.placeCenter()
        mainFrame.pack(side="top")
        frameBTN.pack(side="bottom")

        btnLinkSource.placeRightCenter()
        btnLinkWeb.placeLeftCenter()
