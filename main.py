from arrera_tk.arrera_tk import *
topLevel_active = False
button_active = False
label_active = False
frame_active = False
about_active = False
entry_active = False
text_box_active = False

def gestion():
    global topLevel_active, button_active, label_active,frame_active,about_active,entry_active,text_box_active
    
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


    w.mainloop()


def main():
    global topLevel_active, button_active, label_active,frame_active,about_active,entry_active,text_box_active
    
    print("Menu texte Arrera TK\n")
    var = 1
    while var != 0:
        ok = False
        while not ok:
            try :
                var = int(input("1.TopLevel\n2.Button\n"
                                "3.Label\n4.Frame\n"
                                "5.A Propos\n6.Entry\n"
                                "7.TextBox\n"
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
            case 0:
                print("Lancement de l'interface...")

    gestion()

if __name__ == "__main__":
    main()