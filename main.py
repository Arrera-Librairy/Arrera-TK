from arrera_tk.arrera_tk import *
topLevel_active = False
button_active = False
label_active = False

def gestion():
    global topLevel_active, button_active, label_active
    
    w = aTk(title="Teste Arrera TK")

    if label_active:
        label = aLabel(w, text="Super label")
        label.pack(pady=20)
    
    if button_active:
        btn = aButton(w, text="Super bouton")
        btn.pack(pady=20)

    if topLevel_active:
        topLevel = aTopLevel(title="Fenêtre secondaire")

    w.mainloop()


def main():
    global topLevel_active, button_active, label_active
    
    print("Menu texte Arrera TK\n")
    var = 1
    while var != 0:
        ok = False
        while not ok:
            try :
                var = int(input("1.TopLevel\n2.Button\n"
                                "3.Label\n0.Lancer\n# "))
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
            case 0:
                print("Lancement de l'interface...")

    gestion()

if __name__ == "__main__":
    main()