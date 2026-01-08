from arrera_tk.arrera_tk import *
topLevel_active = False
button_active = False
label_active = False
frame_active = False
about_active = False
entry_active = False
text_box_active = False
checkbox_active = False
radio_button_active = False
scrollableframe_active = False
canvas_active = False
backgroundimage_active = False
textbox_scroll_active = False

def gestion():
    global topLevel_active, button_active, label_active,frame_active,about_active,entry_active,text_box_active, \
        checkbox_active,radio_button_active,scrollableframe_active,canvas_active,backgroundimage_active,textbox_scroll_active
    
    w = aTk(title="Teste Arrera TK")

    if label_active:
        label = aLabel(w, text="Super label")
        label.pack(pady=20)
    
    if button_active:
        btn = aButton(w, text="Super bouton")
        btn.pack(pady=20)

    if topLevel_active:
        topLevel = aTopLevel(title="Fenêtre secondaire")

    if frame_active :
        frame = aFrame(w,fg_color="red")
        aButton(frame, text="btn Frame").place(x=0,y=0)
        frame.pack()

    if about_active :
        windows_about("ArreraTK Teste",
                      "image/test.png",
                      "I2026",
                      "MOI",
                      "www.arrera-software.fr",
                      "www.google.com")
    if entry_active :
        entry = aEntry(w)
        entry.pack()

    if text_box_active :
        text = aText(w,center=True)
        text.pack()

    if checkbox_active:
        checkbox = aCheckBox(w,True)
        print("Checkbox : ",checkbox.getBooleanVar)
        checkbox.pack()

    if radio_button_active:
        radio = aRadioButton(w)
        radio.pack()

    if scrollableframe_active:
        scrollableframe = aScrollableFrame(w)
        scrollableframe.pack()

    if canvas_active:
        canvas = aCanvas(w)
        canvas.pack()

    if backgroundimage_active:
        bimage = aBackgroundImage(w,"image/test.png","image/test2.png")
        bimage.pack()

    if textbox_scroll_active :
        textbox_scroll = aTextScrollable(w)
        textbox_scroll.enableTextBox()
        textbox_scroll.pack()

    w.mainloop()


def main():
    global topLevel_active, button_active, label_active,frame_active,about_active,entry_active,text_box_active, \
        checkbox_active,radio_button_active,scrollableframe_active,canvas_active,backgroundimage_active,textbox_scroll_active

    print("Menu texte Arrera TK\n")
    var = 1
    while var != 0:
        ok = False
        while not ok:
            try :
                var = int(input("1.TopLevel\n2.Button\n"
                                "3.Label\n4.Frame\n"
                                "5.A Propos\n6.Entry\n"
                                "7.TextBox\n8.Checkbox\n"
                                "9.RadioButton\n10.ScrollableFrame\n"
                                "11.Canvas\n12.Background Image\n"
                                "13.Text Box Scroll\n"
                                "0.Lancer\n# "))
                ok = True
            except ValueError:
                print("Valeur invalide")
                ok = False

        match(var):
            case 1 :
                topLevel_active = True
                print("TopLevel Activé")
            case 2 :
                button_active = True
                print("Button Activé")
            case 3 :
                label_active = True
                print("Label Activé")
            case 4 :
                frame_active = True
                print("Frame Activer")
            case 5 :
                about_active = True
                print("About Activer")
            case 6 :
                entry_active = True
                print("Entry Activer")
            case 7 :
                text_box_active = True
                print("Text Box Activer")
            case 8 :
                checkbox_active = True
                print("Checkbox Activer")
            case 9 :
                radio_button_active = True
                print("RadioButton Activer")
            case 10:
                scrollableframe_active = True
                print("ScrollableFrame Activer")
            case 11 :
                canvas_active = True
                print("Canvas Activer")
            case 12 :
                backgroundimage_active = True
                print("Background Image Activer")
            case 13 :
                textbox_scroll_active = True
                print("Text Box Scroll Activer")
            case 0:
                print("Lancement de l'interface...")

    gestion()

if __name__ == "__main__":
    main()