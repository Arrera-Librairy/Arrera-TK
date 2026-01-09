# Arrera TK

[French version](README.md)

Arrera TK is a Python library using Tkinter and CustomTkinter, with a custom theme inspired by Material 3 Expressive.

## Themes available with the library

- white
- blue/grey
- blue
- blue/white
- blue/purple
- grey
- yellow
- orange
- pink
- red

## Explanation of how themes work

To use an Arrera TK theme, you must choose the theme you want to use, place it in a folder in your project, and indicate its location in the main window creation object (`aTk` with the `theme_file` argument).
By default, if you do not specify a theme, the program will look for its default theme at `theme/theme_default.json`.

## Usage

To use Arrera TK, download the `arrera_tk.py` file and import it into your project. Install the dependencies present in the `requirements.txt` file using the following command:

```bash
pip install -r requirements.txt
```
And finally, import the module into your project:
```python
from arrera_tk import *
```

## Methods details

### Widgets

*   **aLabel**: Basic label.
*   **aButton**: Standard button.
*   **aCheckBox**: Checkbox.
*   **aRadioButton**: Radio button.
*   **aEntry**: Text entry field.
*   **aText**: Multiline text area.
*   **aTextScrollable**: Text area with scrollbar.
*   **aEntryLengend**: Entry field accompanied by a descriptive label.
*   **aOptionMenu**: Dropdown menu.
*   **aOptionMenuLengend**: Dropdown menu accompanied by a descriptive label.
*   **aHourPickers**: Hour and minute selector.
*   **aSwicht**: On/off switch.

### Containers (Frames)

*   **aFrame**: Simple container with rounded corners.
*   **aScrollableFrame**: Container with scrolling.
*   **aCanvas**: Drawing area.
*   **aBackgroundImage**: Container with a background image.

### Windows

*   **aTk**: Main application window. Manages the theme and icon.
*   **aTopLevel**: Secondary window.
*   **windows_about**: Pre-configured "About" window.

### Placement

Widgets inherit methods facilitating their positioning.

#### Place
These methods use `place()` with relative coordinates to position elements.

*   **Centered**: `placeCenter()`
*   **Corners**: `placeTopLeft()`, `placeTopRight()`, `placeBottomLeft()`, `placeBottomRight()`
*   **Centered Edges**: `placeTopCenter()`, `placeBottomCenter()`, `placeLeftCenter()`, `placeRightCenter()`
*   **Specific**:
    *   `placeCenterOnWidth(y)`: Centers horizontally at the given Y position.
    *   `placeWidgetCenteredAtBottom(x_offset)`: Centers at the bottom with an optional X offset.
    *   `placeLeftBottomNoStick()`, `placeRightBottomNoStick()`, `placeBottomCenterNoStick()`: Places at the bottom (left, right, or center) with a 10px margin to avoid sticking to the edge.

#### Pack
These methods use `pack()` to stack elements. They accept `xExpand` (bool) and `yExpand` (bool) arguments to manage expansion in the corresponding directions.

*   `pack(xExpand, yExpand)`: Standard pack.
*   `packLeft(xExpand, yExpand)`: Pack aligned to the left.
*   `packRight(xExpand, yExpand)`: Pack aligned to the right.
*   `packTop(xExpand, yExpand)`: Pack aligned to the top.
*   `packBottom(xExpand, yExpand)`: Pack aligned to the bottom.
