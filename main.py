from arrera_tk.arrera_tk import *

def main():
    a = aTk(icon="image/test.png")
    b = aTopLevel()
    btn = aButton(a)
    btn.pack()
    a.mainloop()

if __name__ == "__main__":
    main()