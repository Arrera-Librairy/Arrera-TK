import customtkinter as ctk
from PIL import Image
from .utils import resource_path

class aImage(ctk.CTkImage):
    def __init__(self, width: int, height: int, path_light: str, path_dark: str = ""):
        if path_dark != "":
            super().__init__(light_image=Image.open(resource_path(path_light)),
                             dark_image=Image.open(resource_path(path_dark)),
                             size=(width, height))
        else:
            super().__init__(light_image=Image.open(resource_path(path_light)), size=(width, height))
