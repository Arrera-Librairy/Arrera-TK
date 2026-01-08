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
entry_legend_active = False
optionmenu_active = False
optionmenu_legend_active = False
hour_pickers_active = False
swicht_active = False
test_placement_active = False

theme = ""
dictTheme = {
"default":"theme/theme_default.json",
"Blanc/Gris":"theme/theme_blanc_gris.json",
"Bleu/Blanc":"theme/theme_bleu_blanc.json",
"Bleu/Violet":"theme/theme_bleu_violet.json",
"orange":"theme/theme_orange.json",
"rouge":"theme/theme_rouge.json",
"rose":"theme/theme_rose.json",
"bleu":"theme/theme_bleu.json",
"jaune":"theme/theme_jaune.json",
"blanc":"theme/theme_blanc.json",
"gris":"theme/theme_gris.json"
}

def checkSwictBTN(s:aSwicht):
    print(s.getValue())

def setTheme():
    global theme,dictTheme

    print("Choix du theme d'Arrera TK")

    var = 1

    ok = False
    while not ok:
        try :
            var = int(input("1.Blanc/Gris\n2.Bleu/Blanc\n3.Bleu/Violet\n4.Orange\n5.Rouge\n6.Rose\n7.Bleu\n8.Jaune\n9.Blanc\n"
                            "\n0.Theme par default\n# "))
            ok = True
        except ValueError:
            print("Valeur invalide")
            ok = False

    theme = list(dictTheme.keys())[var]



def gestion():
    global topLevel_active, button_active, label_active,frame_active,about_active,entry_active,text_box_active, \
        checkbox_active,radio_button_active,scrollableframe_active,canvas_active,backgroundimage_active,textbox_scroll_active ,\
        entry_legend_active,optionmenu_active,optionmenu_legend_active,hour_pickers_active,swicht_active,test_placement_active,theme,dictTheme
    
    w = aTk(title="Teste Arrera TK",theme_file=dictTheme[theme])

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

    if entry_legend_active :
        entry_legend = aEntryLengend(w)
        entry_legend.pack()

    if optionmenu_active :
        super_list = ["Option 1","Option 2","Option 3"]
        optionmenu = aOptionMenu(w,value=super_list)
        optionmenu.pack()
        print(optionmenu.getValue())

    if optionmenu_legend_active:
        super_list = ["Option 1","Option 2","Option 3"]
        optionmenu_legend = aOptionMenuLengend(w,values=super_list)
        optionmenu_legend.pack()
        print(optionmenu_legend.getValue())

    if hour_pickers_active:
        hour_pickers = aHourPickers(w)
        hour_pickers.pack()

    if swicht_active:
        swicht = aSwicht(w,command=lambda : checkSwictBTN(swicht))
        swicht.pack()

    if test_placement_active:
        aLabel(w,text="Haut gauche").placeTopLeft()
        aLabel(w,text="Haut droite").placeTopRight()
        aLabel(w,text="Bas gauche").placeBottomLeft()
        aLabel(w,text="Bas droite").placeBottomRight()
        aLabel(w,text="Centre").placeCenter()
        aLabel(w,text="Centre gauche").placeLeftCenter()
        aLabel(w,text="Centre droite").placeRightCenter()
        aLabel(w,text="Haut centre").placeTopCenter()
        aLabel(w,text="Bas centre").placeBottomCenter()
        aLabel(w,text="Center on width").placeCenterOnWidth(y=30)
        aLabel(w,text="placeWidgetCenteredAtBottom").placeWidgetCenteredAtBottom(x_offset=15)
        aLabel(w,text="En bas a droite").placeBottomRight()
        aLabel(w,text="En bas a gauche").placeBottomLeft()
        aLabel(w,text="En haut a droite").placeTopRight()

    w.mainloop()


def main():
    global topLevel_active, button_active, label_active,frame_active,about_active,entry_active,text_box_active, \
        checkbox_active,radio_button_active,scrollableframe_active,canvas_active,backgroundimage_active,textbox_scroll_active , \
        entry_legend_active,optionmenu_active,optionmenu_legend_active,hour_pickers_active,swicht_active,test_placement_active


    setTheme()

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
                                "13.Text Box Scroll\n14.Entry Lengend\n"
                                "15.Option Menu\n16.Option Menu Lengend\n"
                                "17.Hour pickers\n18.Swicht\n"
                                "19.Test Placement\n"
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
            case 14 :
                entry_legend_active = True
                print("Entry Legend Activer")
            case 15:
                optionmenu_active = True
                print("Option Menu Activer")
            case 16:
                optionmenu_legend_active = True
                print("Option Menu Legend Activer")
            case 17:
                hour_pickers_active = True
                print("Hour Pickers Activer")
            case 18:
                swicht_active = True
                print("Swicht Activer")
            case 19 :
                test_placement_active = True
                print("Test Placement Activer")
            case 0:
                print("Lancement de l'interface...")

    gestion()

if __name__ == "__main__":
    main()