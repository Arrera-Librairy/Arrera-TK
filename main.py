from venv import create

from arrera_tk.arrera_tk import *

def test(input):
    print(input)

def main():
    atk = CArreraTK()
    screen = atk.aTK(1)
    atk.title("Super windows")
    atk.setColor("red", "white")
    label = atk.createLabel(screen,"Je suis trop fort")
    label.pack()
    btn = atk.createButton(screen,"Je suis un bouton",command=lambda: test("Je suis un bouton"))
    entry = atk.createEntry(screen)
    entry.pack()
    btn.pack()
    atk.view()# This will create a Tkinter window with the title "Super windows" and resizable
    pass

if __name__ == '__main__':
    main()