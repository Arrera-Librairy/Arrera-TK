import customtkinter as ctk
from PIL import Image
from .utils import resource_path

class aBackgroundImage(ctk.CTkFrame):
    def __init__(self, master, background_light: str, background_dark: str = "", height: int = 600, width: int = 800,
                 **kwargs):
        super().__init__(master, **kwargs)

        self.__size = (width, height)
        self.configure(width=width, height=height, border_width=0)

        # Création de l'image initiale
        background = self._create_ctk_image(background_light, background_dark)

        # Sauvegarde de l'image pour éviter le garbage collection
        self.__current_image = background

        # Utilisation d'un CTkLabel pour afficher l'image
        # Note: Assure-toi que aLabel accepte l'argument 'image' ou utilise ctk.CTkLabel
        self.__label = ctk.CTkLabel(self, text="", image=background)
        self.__label.place(relx=0.5, rely=0.5, anchor='center')

    def _create_ctk_image(self, light_path: str, dark_path: str):
        """Méthode interne pour générer l'objet CTkImage correctement"""
        # Si dark_path est vide, on utilise l'image light pour les deux modes
        path_for_dark = dark_path if dark_path != "" else light_path

        return ctk.CTkImage(
            light_image=Image.open(resource_path(light_path)),
            dark_image=Image.open(resource_path(path_for_dark)),
            size=self.__size
        )

    def change_background(self, background_light: str, background_dark: str = ""):
        """Permet de changer dynamiquement les images de fond"""
        new_background = self._create_ctk_image(background_light, background_dark)

        # Sauvegarde de la nouvelle image pour éviter le garbage collection
        self.__current_image = new_background

        self.__label.configure(image=new_background)
