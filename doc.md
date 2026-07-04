# Arrera-TK Documentation

## Installation

*(To be completed)*

## Widgets

### `aTk`
The main window class for the application.

**Initialization:**
`aTk(title: str = "ArreraTK", width: int = 800, height: int = 600, resizable: bool = False, icon: str = "", theme: str = "defaut", **kwargs)`
- `title`: The title of the window.
- `width`: Window width.
- `height`: Window height.
- `resizable`: Boolean to allow window resizing.
- `icon`: Path to the window icon (`.ico` or `.png`).
- `theme`: The theme to apply (e.g. `"defaut"`, `"blanc"`, `"blanc-gris"`, `"bleu"`, `"bleu-blanc"`, `"bleu-violet"`, `"gris"`, `"jaune"`, `"orange"`, `"rose"`, `"rouge"`).
- `**kwargs`: Additional arguments passed to `ctk.CTk`.

---

### `aTopLevel`
A secondary window (toplevel) class.

**Initialization:**
`aTopLevel(title: str = "Arrera TopLevel", width: int = 400, height: int = 300, resizable: bool = False, icon: str = "", **kwargs)`
- `title`: The title of the secondary window.
- `width`: Window width.
- `height`: Window height.
- `resizable`: Boolean to allow window resizing.
- `icon`: Path to the window icon (`.ico` or `.png`).
- `**kwargs`: Additional arguments passed to `ctk.CTkToplevel`.

---

### `aButton`
A customizable button widget.

**Initialization:**
`aButton(master, text: str = "Arrera Button", width: int = 140, height: int = 40, command=None, size: int = 0, dark_color: str = "", light_color: str = "", light_text_color: str = "", dark_text_color: str = "", **kwargs)`
- `master`: The parent widget.
- `text`: The text displayed on the button.
- `width`: Button width.
- `height`: Button height.
- `command`: Callback function triggered on button press.
- `size`: Font size for the text.
- `dark_color` / `light_color`: Background colors for dark/light modes.
- `dark_text_color` / `light_text_color`: Text colors for dark/light modes.

---

### `aLabel`
A label widget used to display text or images.

**Initialization:**
`aLabel(master, text: str = "Arrera Label", police_size: int = 0, dark_color: str = "", light_color: str = "", light_text_color: str = "", dark_text_color: str = "", image: CTkImage = None, **kwargs)`
- `master`: The parent widget.
- `text`: Text to display.
- `police_size`: Font size.
- `dark_color` / `light_color`: Background colors.
- `dark_text_color` / `light_text_color`: Text colors.
- `image`: An optional `CTkImage` object.

---

### `aImage`
An image widget that supports light and dark modes.

**Initialization:**
`aImage(width: int, height: int, path_light: str, path_dark: str = "")`
- `width`: Image width.
- `height`: Image height.
- `path_light`: Path to the image file (used in light mode, and dark mode if `path_dark` is not provided).
- `path_dark`: Path to the image file used in dark mode.

---

### `aBackgroundImage`
A frame designed to display a background image.

**Initialization:**
`aBackgroundImage(master, background_light: str, background_dark: str = "", height: int = 600, width: int = 800, **kwargs)`

**Methods:**
- `change_background(background_light: str, background_dark: str = "")`: Dynamically change the background images.

---

### `aEntry`
A single-line text entry widget.

**Initialization:**
`aEntry(master, police_size: int = 15, width: int = 20, **kwargs)`

---

### `aEntryLengend`
An entry widget paired with a descriptive label.

**Initialization:**
`aEntryLengend(master, text: str = "Arrera Entry Legend", bg: str = "", fg: str = "", police_size: int = 15, width: int = 200, gridUsed: bool = False)`

**Methods:**
- `getEntry()`: Returns the underlying `aEntry` widget.
- `changeColorLabel(bg: str = "", fg: str = "")`: Updates label colors.
- `changeTextLabel(text: str)`: Updates label text.
- `changePoliceLabel(font)`: Updates label font.

---

### `aText`
A multi-line text box widget.

**Initialization:**
`aText(master, police_size: int = 15, center: bool = False, **kwargs)`

**Methods:**
- `disable_textbox()`: Sets the text box state to disabled.
- `enable_textbox()`: Sets the text box state to normal and focuses it.
- `insert_text(text: str)`: Inserts text at the beginning.
- `centre_text()`: Centers the text.

---

### `aTextScrollable`
A text box widget wrapped in a scrollable frame.

**Initialization:**
`aTextScrollable(master, police_size: int = 15)`

**Methods:**
- `getTextBox()`: Returns the underlying `CTkTextbox`.
- `enableTextBox()`: Sets the state to normal.
- `disableTextBox()`: Sets the state to disabled.

---

### `aCheckBox`
A checkbox widget with a bound `BooleanVar`.

**Initialization:**
`aCheckBox(master, boolean_value: bool, **kwargs)`

**Methods:**
- `getBooleanVar()`: Returns the bound boolean variable.
- `setFalse()`: Sets the checkbox to false.
- `setTrue()`: Sets the checkbox to true.

---

### `aRadioButton`
A radio button widget.

**Initialization:**
`aRadioButton(master, text: str = "Arrera RadioButton", variable=None, value=0, command=None, **kwargs)`

---

### `aSwicht`
A toggle switch widget bound to a `BooleanVar`.

**Initialization:**
`aSwicht(master, text="Arrera Button Swicht", default_value: bool = False, **kwargs)`

**Methods:**
- `setOn()`: Sets the switch on.
- `setOff()`: Sets the switch off.
- `getValue()`: Returns the current boolean value.
- `change_text(text="")`: Updates the switch text.

---

### `aOptionMenu`
A dropdown option menu.

**Initialization:**
`aOptionMenu(master, value: list, police_size: int = 15, bg: str = "", fg: str = "", width: int = 200, **kwargs)`

**Methods:**
- `getValue()`: Returns the current selected value.
- `changeColor(bg: str = "", fg: str = "")`: Updates background and foreground colors.
- `changePolice(font)`: Updates the font.
- `set_text(text: str)`: Sets the displayed text/value.

---

### `aOptionMenuLengend`
An option menu paired with a descriptive label.

**Initialization:**
`aOptionMenuLengend(master, values: list, text: str = "Arrera OptionMenu Legend", bg: str = "", fg: str = "", police_size: int = 15, gridUsed: bool = False)`

**Methods:**
- `getOptionMenu()`: Returns the underlying `aOptionMenu`.
- `getValue()`: Returns the selected value.
- `changeColorLabel(bg: str = "", fg: str = "")`: Updates label colors.
- `changeTextLabel(text: str)`: Updates label text.
- `changePoliceLabel(font)`: Updates label font.
- `set_text(text: str)`: Sets the option menu value.

---

### `aHourPickers`
A set of option menus for selecting hours and minutes.

**Initialization:**
`aHourPickers(master, minute_pickers: bool = False, **kwargs)`

**Methods:**
- `getValueHour()`: Returns selected hour.
- `getValueMinute()`: Returns selected minute.
- `setValueMinute(minute: str)`: Sets minute value.
- `setValueHour(hour: str)`: Sets hour value.

---

### `aFrame`
A frame container widget.

**Initialization:**
`aFrame(master, corner_radius: int = 20, **kwargs)`

---

### `aScrollableFrame`
A scrollable frame container widget.

**Initialization:**
`aScrollableFrame(master, corner_radius: int = 20, **kwargs)`

---

### `aCanvas`
A canvas widget for drawing shapes and custom graphics.

**Initialization:**
`aCanvas(master, **kwargs)`

---

## Utility Layout Methods

All widgets inheriting from `placement_Tool_Kit_internet` (most widgets in this library) also support various layout utility methods for easier positioning.

**Placement Methods:**
- `placeCenter()`: Places the widget exactly in the center of its parent.
- `placeLeftCenter()`: Places the widget vertically centered on the left edge.
- `placeRightCenter()`: Places the widget vertically centered on the right edge.
- `placeTopCenter()`: Places the widget horizontally centered on the top edge.
- `placeBottomCenter()`: Places the widget horizontally centered on the bottom edge.
- `placeCenterOnWidth(y: int = 0)`: Places the widget horizontally centered at a specific `y` vertical coordinate.
- `placeWidgetCenteredAtBottom(x_offset=1)`: Places the widget horizontally centered at the bottom, with a horizontal offset `x_offset`.
- `placeBottomRight()`: Places the widget at the bottom-right corner.
- `placeBottomLeft()`: Places the widget at the bottom-left corner.
- `placeTopRight()`: Places the widget at the top-right corner.
- `placeTopLeft()`: Places the widget at the top-left corner.
- `placeCenterRight()`: Alias for `placeRightCenter()`.
- `placeCenterLeft()`: Alias for `placeLeftCenter()`.
- `placeLeftBottomNoStick()`: Places the widget at the bottom-left corner with some padding (x=10, y=-10).
- `placeRightBottomNoStick()`: Places the widget at the bottom-right corner with some padding (x=-10, y=-10).
- `placeBottomCenterNoStick()`: Places the widget at the bottom-center with some padding (y=-10).

**Pack Methods:**
- `pack(xExpand: bool = False, yExpand: bool = False, **kwargs)`: Standard pack with optional horizontal (`xExpand`) and vertical (`yExpand`) expansion.
- `packLeft(xExpand: bool = False, yExpand: bool = False, **kwargs)`: Packs the widget to the left side (`side="left"`).
- `packRight(xExpand: bool = False, yExpand: bool = False, **kwargs)`: Packs the widget to the right side (`side="right"`).
- `packTop(xExpand: bool = False, yExpand: bool = False, **kwargs)`: Packs the widget to the top side (`side="top"`).
- `packBottom(xExpand: bool = False, yExpand: bool = False, **kwargs)`: Packs the widget to the bottom side (`side="bottom"`).
