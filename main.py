from venv import create

from arrera_tk.arrera_tk import *

def test(input):
    print(input)

def main():
    listValue = ["test1","test2","test3"]
    atk = CArreraTK()
    var = input("Enter 1 for Tkinter, 0 for customtkinter: ")
    if var == "1":
        screen = atk.aTK(1)
    else:
        screen = atk.aTK()
    var = StringVar(screen)
    atk.title("Super windows")
    #atk.setColor("red", "white")
    atk.setResizable(False)
    label = atk.createLabel(screen,"Je suis trop fort")

    btn = atk.createButton(screen,"Je suis un bouton",command=lambda: test("Je suis un bouton"))
    entry = atk.createEntry(screen)
    text = atk.createText(screen)
    checkbox = atk.createCheckbox(screen,"Je suis une checkbox",bg="red",fg="white")
    redioBTN = atk.createRadioButton(screen,"Je suis un radio button")
    canvas = atk.createCanvas(screen,width=50,height=50,bg="pink")
    canvasImage = atk.createCanvas(screen,width=50,height=50,imageFile="image/test.png")
    frame = atk.createFrame(screen)
    optionMenu = atk.createOptionMenu(screen,listValue,var)
    varNB = input("Enter 1 Place, 0 pack : ")
    if varNB == "1":
        atk.placeTopCenter(label)
        atk.placeLeftTop(btn)
        atk.placeRightTop(entry)
        atk.placeLeftBottom(text)
        atk.placeRightBottom(checkbox)
        atk.placeCenter(redioBTN)
        atk.placeLeftCenter(canvas)
        atk.placeRightCenter(canvasImage)
        atk.placeBottomCenter(frame)
    else :
        atk.pack(label)
        atk.packLeft(btn)
        atk.packRight(entry)
        atk.packTop(optionMenu)
        atk.packBottom(checkbox)
    atk.view()# This will create a Tkinter window with the title "Super windows" and resizable

    pass

if __name__ == '__main__':
    main()