# Arrera TK

Arrera TK est une librairie Python utilisant Tkinter et CustomTkinter, avec un thème personnalisé inspiré de Material 3 Expressive.

## Thèmes disponibles avec la librairie

- blanc  
- bleu/gris  
- bleu  
- bleu/blanc  
- bleu/violet  
- gris  
- jaune  
- orange  
- rose  
- rouge  

## Explication du fonctionnement des thèmes

Pour utiliser un thème d’Arrera TK, il faut choisir le thème que vous voulez utiliser, le mettre dans un dossier de votre projet et indiquer son emplacement dans l’objet de la création de la fenêtre principale (`aTk` avec l’argument `theme_file`).  
Par défaut, si vous ne mettez pas de thème, le programme ira chercher son thème par défaut à l’emplacement `theme/theme_default.json`.

## Utilisation

Pour utiliser Arrera TK, téléchargez le fichier `arrera_tk.py` et importez-le dans votre projet. Installez les dépendances présentes dans le fichier `requirements.txt` en utilisant la commande suivante :

```bash
pip install -r requirements.txt
```
Et enfin, importer le module dans votre projet :
```python
from arrera_tk import *
```

## Details des methode 

### Widgets

*   **aLabel** : Label basique.
*   **aButton** : Bouton standard.
*   **aCheckBox** : Case à cocher.
*   **aRadioButton** : Bouton radio.
*   **aEntry** : Champ de saisie de texte.
*   **aText** : Zone de texte multiligne.
*   **aTextScrollable** : Zone de texte avec barre de défilement.
*   **aEntryLengend** : Champ de saisie accompagné d'un label descriptif.
*   **aOptionMenu** : Menu déroulant.
*   **aOptionMenuLengend** : Menu déroulant accompagné d'un label descriptif.
*   **aHourPickers** : Sélecteur d'heure et de minutes.
*   **aSwicht** : Interrupteur on/off.

### Conteneurs (Frames)

*   **aFrame** : Conteneur simple avec coins arrondis.
*   **aScrollableFrame** : Conteneur avec défilement.
*   **aCanvas** : Zone de dessin.
*   **aBackgroundImage** : Conteneur avec une image en arrière-plan.

### Fenêtres

*   **aTk** : Fenêtre principale de l'application. Gère le thème et l'icône.
*   **aTopLevel** : Fenêtre secondaire.
*   **windows_about** : Fenêtre "À propos" pré-configurée.

### Placement

Les widgets héritent de méthodes facilitant leur positionnement.

#### Place
Ces méthodes utilisent `place()` avec des coordonnées relatives pour positionner les éléments.

*   **Centré** : `placeCenter()`
*   **Coins** : `placeTopLeft()`, `placeTopRight()`, `placeBottomLeft()`, `placeBottomRight()`
*   **Bords centrés** : `placeTopCenter()`, `placeBottomCenter()`, `placeLeftCenter()`, `placeRightCenter()`
*   **Spécifique** :
    *   `placeCenterOnWidth(y)` : Centre horizontalement à la position Y donnée.
    *   `placeWidgetCenteredAtBottom(x_offset)` : Centre en bas avec un décalage X optionnel.
    *   `placeLeftBottomNoStick()`, `placeRightBottomNoStick()`, `placeBottomCenterNoStick()` : Place en bas (gauche, droite ou centre) avec une marge de 10px pour ne pas coller au bord.

#### Pack
Ces méthodes utilisent `pack()` pour empiler les éléments. Elles acceptent les arguments `xExpand` (bool) et `yExpand` (bool) pour gérer l'extension dans les directions correspondantes.

*   `pack(xExpand, yExpand)` : Pack standard.
*   `packLeft(xExpand, yExpand)` : Pack aligné à gauche.
*   `packRight(xExpand, yExpand)` : Pack aligné à droite.
*   `packTop(xExpand, yExpand)` : Pack aligné en haut.
*   `packBottom(xExpand, yExpand)` : Pack aligné en bas.