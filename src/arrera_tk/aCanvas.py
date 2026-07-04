import customtkinter as ctk

class aCanvas(ctk.CTkCanvas):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)