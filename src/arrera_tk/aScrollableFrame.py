import customtkinter as ctk
from .placement_Tool_Kit_internet import placement_Tool_Kit_internet

class aScrollableFrame(placement_Tool_Kit_internet, ctk.CTkScrollableFrame):
    def __init__(self, master, corner_radius: int = 20, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=corner_radius)
