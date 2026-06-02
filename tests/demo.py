from tkinter import messagebox

from arrera_tk import *

class arreratk_demo(aTk):
    def __init__(self):
        super().__init__(title="ArreraTK Demon")

        #Scrollable Frame
        main_frame = aScrollableFrame(self)
        main_frame.pack(fill="both", expand=True)

        #aLabel
        aLabel(main_frame, text="aLabel Widget").pack(pady=5)

        # aButton
        aButton(main_frame, text="aButton").pack(pady=5)

        # aCheckBox
        aCheckBox(main_frame, boolean_value=True).pack(pady=5)

        # aRadioButton
        aRadioButton(main_frame, text="aRadioButton").pack(pady=5)

        # aEntry
        aEntry(main_frame, placeholder_text="aEntry").pack(pady=5)

        # aText
        text_widget = aText(main_frame, height=4)
        text_widget.insert("0.0", "aText Widget")
        text_widget.pack(pady=5, padx=10)

        # aTextScrollable
        scroll_text = aTextScrollable(main_frame)
        scroll_text.getTextBox().insert("0.0", "aTextScrollable Widget\\n" * 5)
        scroll_text.pack(pady=5, padx=10)

        # aEntryLengend
        aEntryLengend(main_frame, text="aEntryLengend").pack(pady=10)

        # aOptionMenu
        options = ["Option 1", "Option 2", "Option 3"]
        aOptionMenu(main_frame, value=options).pack(pady=5)

        # aOptionMenuLengend
        aOptionMenuLengend(main_frame, text="aOptionMenuLengend", values=options).pack(pady=10)

        # aHourPickers
        aHourPickers(main_frame).pack(pady=5)

        # aSwicht
        aSwicht(main_frame, text="aSwicht").pack(pady=5)

        # aFrame
        frame = aFrame(main_frame, height=50, width=200)
        frame.pack(pady=5)
        aLabel(frame, text="Inside aFrame").place(relx=0.5, rely=0.5, anchor="center")

        # aCanvas
        canvas = aCanvas(main_frame)
        canvas.create_line(0, 0, 200, 50, fill="red", width=3)
        canvas.pack(pady=5)

        # aImage (requires a placeholder image)
        img = aImage(path_light="test-image/placeholder.png", width=100, height=50)
        aLabel(main_frame, image=img).pack(pady=5)

        aButton(main_frame,text="Open TopLevel",command=self.__open_top_level).pack(pady=5)
        aButton(main_frame, text="Open About Window", command= lambda :
        windows_about(nameSoft="Arrera Tk About",
                      iconFile='test-image/test.png',
                      version="3.0.0",
                      copyright="rien",
                      linkWeb="www.arrera-software.fr",
                      linkSource="www.arrera-software.fr")
                ).pack(pady=5)


    def __open_top_level(self):
        top = aTopLevel()
        aLabel(top, text="This is a TopLevel Window").pack(pady=20)

    """
    def __windows_theme(self):
        w = aTopLevel(title="Gestion themes",width=400,height=300,resizable=False)

        self.__view_theme = aLabel(w,text="Theme actuel : "+self.get_current_theme(),police_size=25)

        self.__menu_theme = aOptionMenuLengend(w,text="Themes ",values=self.get_list_theme())

        btn_change = aButton(w,text="Changer",command=self.__update_theme)

        self.__view_theme.placeTopCenter()
        self.__menu_theme.placeCenter()
        btn_change.placeBottomCenter()


    def __update_theme(self):
        theme = self.__menu_theme.getValue()
        if self.change_theme(theme):
            self.__view_theme.configure(text="Theme actuel : "+self.get_current_theme())
            messagebox.showinfo("Succès", f"Thème changé en {theme}")
    """

    def view(self):
        #self.__windows_theme()
        self.mainloop()

arreratk_demo().view()