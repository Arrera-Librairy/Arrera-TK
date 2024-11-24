from venv import create

from arrera_tk.arrera_tk import *

def test(input):
    print(input)

def main():
    atk = CArreraTK()
    var = input("Enter 1 for Tkinter, 0 for customtkinter: ")
    if var == "1":
        screen = atk.aTK(1)
    else:
        screen = atk.aTK()
    atk.title("Super windows")
    atk.setColor("red", "white")
    label = atk.createLabel(screen,"Je suis trop fort")
    label.pack()
    btn = atk.createButton(screen,"Je suis un bouton",command=lambda: test("Je suis un bouton"))
    entry = atk.createEntry(screen)
    text = atk.createText(screen)
    checkbox = atk.createCheckbox(screen,"Je suis une checkbox",bg="red",fg="white")
    redioBTN = atk.createRadioButton(screen,"Je suis un radio button")
    checkbox.pack()
    entry.pack()
    btn.pack()
    text.pack()
    redioBTN.pack()
    atk.view()# This will create a Tkinter window with the title "Super windows" and resizable

    pass

if __name__ == '__main__':
    main()