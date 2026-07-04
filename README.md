# Arrera TK

[French version](README_fr.md)

Arrera TK is a Python library using Tkinter and CustomTkinter, with a custom theme inspired by Material 3 Expressive.

## Themes available with the library

- `defaut` (Default theme)
- `blanc`
- `blanc-gris`
- `bleu`
- `bleu-blanc`
- `bleu-violet`
- `gris`
- `jaune`
- `orange`
- `rose`
- `rouge`

## Explanation of how themes work

To use an Arrera TK theme, simply pass its name as an argument when creating the main `aTk` window.

```python
# Example of using a theme
app = aTk(theme="bleu") 
```

By default, if no theme is specified, the `defaut` theme will be used. It is also still possible to load a custom theme from a `.json` file by passing the file path to the `theme` argument.

## Installation

### Via PyPI (Recommended)

To use Arrera TK, install the package via pip:

```bash
pip install arrera-tk
```

### From the GitHub repository (Development version)

If you want to use the latest development version, you can install the library directly from GitHub:

```bash
pip install git+https://github.com/Arrera-Software/Arrera-TK.git
```

## Usage

Import the necessary classes into your project:
```python
from arrera_tk import aTk, aButton, aLabel
# Or import the whole module (not recommended for large projects)
# from arrera_tk import *
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
*   **aImage**: Widget to display images, with support for light and dark themes.

### Containers (Frames)

*   **aFrame**: Simple container with rounded corners.
*   **aScrollableFrame**: Container with scrolling.
*   **aCanvas**: Drawing area.
*   **aBackgroundImage**: Container with a background image.

### Windows

*   **aTk**: Main application window. Manages the theme and icon.
*   **aTopLevel**: Secondary window.
*   **windows_about**: Pre-configured "About" window.

### Utilities

*   **keyboad_manager**: Utility to manage keyboard events (associate functions with keys).

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