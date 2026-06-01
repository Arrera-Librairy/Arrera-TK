import os
import sys

sys.path.insert(0, os.path.abspath("src"))

from arrera_tk import *
from PIL import Image

# Create the main window
win = aTk(title="Arrera TK Widgets Showcase")

# Create a scrollable frame to hold the widgets
main_frame = aScrollableFrame(win)
main_frame.pack(fill="both", expand=True)

# --- Widget Showcase ---

# aLabel
aLabel(main_frame, text="aLabel Widget").pack(pady=5)

# aButton
aButton(main_frame, text="aButton").pack(pady=5)

# aCheckBox
aCheckBox(main_frame,boolean_value=True).pack(pady=5)

# aRadioButton
aRadioButton(main_frame, text="aRadioButton").pack(pady=5)

# aEntry
aEntry(main_frame, placeholder_text="aEntry").pack(pady=5)

# aText
text_widget = aText(main_frame, height=4)
text_widget.insert("0.0", "aText Widget")
text_widget.pack(pady=5, padx=10)

# aTextScrollable
scroll_text = aTextScrollable(main_frame)
scroll_text.getTextBox().insert("0.0", "aTextScrollable Widget\\n" * 5)
scroll_text.pack(pady=5, padx=10)

# aEntryLengend
aEntryLengend(main_frame, text="aEntryLengend").pack(pady=10)

# aOptionMenu
options = ["Option 1", "Option 2", "Option 3"]
aOptionMenu(main_frame, value=options).pack(pady=5)

# aOptionMenuLengend
aOptionMenuLengend(main_frame, text="aOptionMenuLengend", values=options).pack(pady=10)

# aHourPickers
aHourPickers(main_frame).pack(pady=5)

# aSwicht
aSwicht(main_frame, text="aSwicht").pack(pady=5)

# aFrame
frame = aFrame(main_frame, height=50, width=200)
frame.pack(pady=5)
aLabel(frame, text="Inside aFrame").place(relx=0.5, rely=0.5, anchor="center")

# aCanvas
canvas = aCanvas(main_frame)
canvas.create_line(0, 0, 200, 50, fill="red", width=3)
canvas.pack(pady=5)

# aImage (requires a placeholder image)
try:
    # Create a dummy image if none exists
    if not os.path.exists("test-image/placeholder.png"):
        img = Image.new('RGB', (100, 50), color = 'gray')
        img.save('test-image/placeholder.png')
    
    img = aImage(path_light="test-image/placeholder.png",width=100, height=50)
    aLabel(main_frame,image=img).pack(pady=5)
except Exception as e:
    print(f"Could not load image for aImage: {e}")
    aLabel(main_frame, text="aImage (placeholder not found)").pack(pady=5)


# --- Toplevel and About Windows ---

def open_toplevel():
    top = aTopLevel(title="Top Level Window")
    aLabel(top, text="This is a TopLevel window").pack(padx=20, pady=20)

def open_about():
    windows_about(nameSoft="Arrera Tk About",
                      iconFile='test-image/test.png',
                      version="3.0.0",
                      copyright="rien",
                      linkWeb="www.arrera-software.fr",
                      linkSource="www.arrera-software.fr")

aButton(main_frame, text="Open aTopLevel", command=open_toplevel).pack(pady=5)
aButton(main_frame, text="Open About Window", command=open_about).pack(pady=5)


# Start the main loop
win.mainloop()
