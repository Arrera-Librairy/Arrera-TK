import platform
import os
import sys

# Fonction pour gerer les resource sur mac os
def resource_path(relative_path):
    if platform.system() == "Darwin":
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath(""), relative_path)
    else:
        return relative_path

def placeLeftTop(widget):
    widget.place(relx=0, rely=0, anchor='nw')


def placeRightTop(widget):
    widget.place(relx=1, rely=0, anchor='ne')


def placeLeftBottom(widget):
    widget.place(relx=0, rely=1, anchor='sw')


def placeRightBottom(widget):
    widget.place(relx=1, rely=1, anchor='se')


def placeCenter(widget):
    widget.place(relx=0.5, rely=0.5, anchor='center')


def placeLeftCenter(widget):
    widget.place(relx=0, rely=0.5, anchor='w')


def placeRightCenter(widget):
    widget.place(relx=1, rely=0.5, anchor='e')


def placeTopCenter(widget):
    widget.place(relx=0.5, rely=0, anchor='n')


def placeBottomCenter(widget):
    widget.place(relx=0.5, rely=1, anchor='s')


def placeCenterOnWidth(widget, y: int = 0):
    if y == 0:
        return
    else:
        widget.place(relx=0.5, y=y, anchor='n')


def placeWidgetCenteredAtBottom(widget, x_offset=1):
    widget.place(relx=0.5, rely=1, x=-x_offset, anchor="s")


def placeBottomRight(widget):
    widget.place(relx=1, rely=1, anchor='se')


def placeBottomLeft(widget):
    widget.place(relx=0, rely=1, anchor='sw')


def placeTopRight(widget):
    widget.place(relx=1, rely=0, anchor='ne')


def placeTopLeft(widget):
    widget.place(relx=0, rely=0, anchor='nw')


def placeCenterRight(widget):
    widget.place(relx=1, rely=0.5, anchor='e')


def placeCenterLeft(widget):
    widget.place(relx=0, rely=0.5, anchor='w')


def placeLeftBottomNoStick(widget):
    widget.place(relx=0, rely=1, anchor='sw', x=10, y=-10)


def placeRightBottomNoStick(widget):
    widget.place(relx=1, rely=1, anchor='se', x=-10, y=-10)


def placeBottomCenterNoStick(widget):
    widget.place(relx=0.5, rely=1, anchor='s', x=0, y=-10)


# Pack

def pack(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both")
    elif xExpand:
        widget.pack(expand=True, fill="x")
    elif yExpand:
        widget.pack(expand=True, fill="y")
    else:
        widget.pack()


def packLeft(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both", side="left")
    elif xExpand:
        widget.pack(expand=True, fill="x", side="left")
    elif yExpand:
        widget.pack(expand=True, fill="y", side="left")
    else:
        widget.pack(side="left")


def packRight(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both", side="right")
    elif xExpand:
        widget.pack(expand=True, fill="x", side="right")
    elif yExpand:
        widget.pack(expand=True, fill="y", side="right")
    else:
        widget.pack(side="right")


def packTop(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both", side="top")
    elif xExpand:
        widget.pack(expand=True, fill="x", side="top")
    elif yExpand:
        widget.pack(expand=True, fill="y", side="top")
    else:
        widget.pack(side="top")


def packBottom(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both", side="bottom")
    elif xExpand:
        widget.pack(expand=True, fill="x", side="bottom")
    elif yExpand:
        widget.pack(expand=True, fill="y", side="bottom")
    else:
        widget.pack(side="bottom")
