import importlib.metadata

try:
    VERSIONARRERATK = importlib.metadata.version("arrera-tk")
except importlib.metadata.PackageNotFoundError:
    VERSIONARRERATK = "0.0.0-local"

from .utils import (
    resource_path, placeLeftTop, placeRightTop, placeLeftBottom, placeRightBottom,
    placeCenter, placeLeftCenter, placeRightCenter, placeTopCenter, placeBottomCenter,
    placeCenterOnWidth, placeWidgetCenteredAtBottom, placeBottomRight, placeBottomLeft,
    placeTopRight, placeTopLeft, placeCenterRight, placeCenterLeft,
    placeLeftBottomNoStick, placeRightBottomNoStick, placeBottomCenterNoStick,
    pack, packLeft, packRight, packTop, packBottom
)

from .placement_Tool_Kit_internet import placement_Tool_Kit_internet
from .aImage import aImage
from .aLabel import aLabel
from .aButton import aButton
from .aCheckBox import aCheckBox
from .aRadioButton import aRadioButton
from .aEntry import aEntry
from .aText import aText
from .aTextScrollable import aTextScrollable
from .aEntryLengend import aEntryLengend
from .aOptionMenu import aOptionMenu
from .aOptionMenuLengend import aOptionMenuLengend
from .aHourPickers import aHourPickers
from .aSwicht import aSwicht
from .aFrame import aFrame
from .aScrollableFrame import aScrollableFrame
from .aCanvas import aCanvas
from .aBackgroundImage import aBackgroundImage
from .aTk import aTk, list_theme
from .aTopLevel import aTopLevel
from .windows_about import windows_about
from .keyboad_manager import keyboad_manager
from .theme import *

__all__ = [
    "VERSIONARRERATK",
    "resource_path",
    "placeLeftTop", "placeRightTop", "placeLeftBottom", "placeRightBottom",
    "placeCenter", "placeLeftCenter", "placeRightCenter", "placeTopCenter", "placeBottomCenter",
    "placeCenterOnWidth", "placeWidgetCenteredAtBottom", "placeBottomRight", "placeBottomLeft",
    "placeTopRight", "placeTopLeft", "placeCenterRight", "placeCenterLeft",
    "placeLeftBottomNoStick", "placeRightBottomNoStick", "placeBottomCenterNoStick",
    "pack", "packLeft", "packRight", "packTop", "packBottom",
    "placement_Tool_Kit_internet",
    "aImage",
    "aLabel",
    "aButton",
    "aCheckBox",
    "aRadioButton",
    "aEntry",
    "aText",
    "aTextScrollable",
    "aEntryLengend",
    "aOptionMenu",
    "aOptionMenuLengend",
    "aHourPickers",
    "aSwicht",
    "aFrame",
    "aScrollableFrame",
    "aCanvas",
    "aBackgroundImage",
    "aTk",
    "aTopLevel",
    "windows_about",
    "keyboad_manager",
    "theme_defaut",
    "theme_blanc",
    "theme_blanc_gris",
    "theme_bleu",
    "theme_bleu_blanc",
    "theme_bleu_violet",
    "theme_gris",
    "theme_jaune",
    "theme_orange",
    "theme_rose",
    "theme_rouge",
    "list_theme"
]
