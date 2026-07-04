from tkinter import messagebox
from arrera_tk import *

class arreratk_demo(aTk):
    def __init__(self,theme:str="defaut"):
        super().__init__(title="ArreraTK Demon", width=800, height=600,theme=theme)

        # Le ScrollableFrame prend toute la place
        scroll_frame = aScrollableFrame(self)
        scroll_frame.pack(fill="both", expand=True)

        # Un Frame à l'intérieur du ScrollableFrame qui contiendra la grille
        # C'est ce Frame qui va s'étendre pour afficher tous les widgets
        grid_container = aFrame(scroll_frame)
        grid_container.pack(fill="both", expand=True)
        
        # Configurer la grille à l'intérieur du grid_container
        grid_container.grid_columnconfigure((0, 1, 2), weight=1) # Permet aux colonnes de s'étirer

        # --- Widgets dans la grille ---

        # Ligne 0
        aLabel(grid_container, text="aLabel Widget").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        aButton(grid_container, text="aButton").grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        aCheckBox(grid_container, boolean_value=True).grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # Ligne 1
        aRadioButton(grid_container, text="aRadioButton").grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        aEntry(grid_container, placeholder_text="aEntry").grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        aSwicht(grid_container, text="aSwicht").grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        # Ligne 2 : Widgets textuels
        text_widget = aText(grid_container, height=4)
        text_widget.insert("0.0", "aText Widget")
        text_widget.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")

        scroll_text = aTextScrollable(grid_container)
        scroll_text.getTextBox().insert("0.0", "aTextScrollable Widget\\n" * 5)
        scroll_text.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Ligne 3
        aEntryLengend(grid_container, text="aEntryLengend").grid(row=3, column=0, columnspan=1, padx=10, pady=10, sticky="ew")
        
        options = ["Option 1", "Option 2", "Option 3"]
        aOptionMenu(grid_container, value=options).grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        
        aOptionMenuLengend(grid_container, text="aOptionMenuLengend", values=options).grid(row=3, column=2, padx=10, pady=10, sticky="ew")

        # Ligne 4
        aHourPickers(grid_container).grid(row=4, column=0, padx=10, pady=10)
        
        frame = aFrame(grid_container, height=50)
        frame.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
        aLabel(frame, text="Inside aFrame").place(relx=0.5, rely=0.5, anchor="center")

        try:
            img = aImage(path_light="test-image/placeholder.png", width=100, height=50)
            aLabel(grid_container, image=img).grid(row=4, column=2, padx=10, pady=10)
        except:
            aLabel(grid_container, text="Image not found").grid(row=4, column=2, padx=10, pady=10)

        # Ligne 5 : Canvas
        canvas = aCanvas(grid_container)
        canvas.create_line(0, 0, 200, 50, fill="red", width=3)
        canvas.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Ligne 6 : Boutons d'action
        aButton(grid_container, text="Open TopLevel", command=self.__open_top_level).grid(row=6, column=0, padx=10, pady=10, sticky="ew")
        
        aButton(grid_container, text="Open About Window", command= lambda :
        windows_about(nameSoft="Arrera Tk About",
                      iconFile='test-image/test.png',
                      version="3.0.0",
                      copyright="rien",
                      linkWeb="www.arrera-software.fr",
                      linkSource="www.arrera-software.fr")
                ).grid(row=6, column=1, columnspan=2, padx=10, pady=10, sticky="ew")


    def __open_top_level(self):
        top = aTopLevel()
        aLabel(top, text="This is a TopLevel Window").pack(pady=20)

    def view(self):
        self.mainloop()

if __name__ == "__main__":
    arreratk_demo().view()
