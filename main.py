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
    atk.setResizable(True)
    label = atk.createLabel(screen,"Je suis trop fort")
    label.pack()
    btn = atk.createButton(screen,"Je suis un bouton",command=lambda: test("Je suis un bouton"))
    entry = atk.createEntry(screen)
    text = atk.createText(screen)
    checkbox = atk.createCheckbox(screen,"Je suis une checkbox",bg="red",fg="white")
    redioBTN = atk.createRadioButton(screen,"Je suis un radio button")
    canvas = atk.createCanvas(screen,width=50,height=50,bg="pink")
    canvasImage = atk.createCanvas(screen,width=50,height=50,imageFile="image/test.png")
    frame = atk.createFrame(screen)
    optionMenu = atk.createOptionMenu(screen,listValue,var)
    checkbox.pack()
    entry.pack()
    btn.pack()
    text.pack()
    redioBTN.pack()
    canvas.pack()
    canvasImage.pack()
    frame.pack()
    optionMenu.pack()
    atk.view()# This will create a Tkinter window with the title "Super windows" and resizable

    pass

if __name__ == '__main__':
    main()