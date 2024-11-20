from arrera_tk.arrera_tk import *

def main():
    atk = CArreraTK()
    screen = atk.aTK()
    atk.title("Super windows")
    atk.setColor("red", "white")
    image = atk.createImage("/home/baptistep/Images/sable_desktop.PNG")
    label = ctk.CTkLabel(screen,image=image).pack()
    atk.view()# This will create a Tkinter window with the title "Super windows" and resizable
    pass

if __name__ == '__main__':
    main()