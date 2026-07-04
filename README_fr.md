# Arrera TK

[English version](README.md)

Arrera TK est une librairie Python utilisant Tkinter et CustomTkinter, avec un thème personnalisé inspiré de Material 3 Expressive.

## Thèmes disponibles avec la librairie

- `defaut` (Thème par défaut)
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

## Explication du fonctionnement des thèmes

Pour utiliser un thème d'Arrera TK, il suffit de passer son nom en argument lors de la création de la fenêtre principale `aTk`.

```python
# Exemple d'utilisation d'un thème
app = aTk(theme="bleu") 
```

Par défaut, si aucun thème n'est spécifié, le thème `defaut` sera utilisé. Il est également toujours possible de charger un thème personnalisé depuis un fichier `.json` en passant le chemin du fichier à l'argument `theme`.

## Installation

### Via PyPI (Recommandé)

Pour utiliser Arrera TK, installez le paquet via pip :

```bash
pip install arrera-tk
```

### Depuis le dépôt GitHub (Version de développement)

Si vous souhaitez utiliser la dernière version de développement, vous pouvez installer la librairie directement depuis GitHub :

```bash
pip install git+https://github.com/Arrera-Software/Arrera-TK.git
```

## Utilisation

Importez les classes nécessaires dans votre projet :
```python
from arrera_tk import aTk, aButton, aLabel
# Ou importez tout le module (non recommandé pour les gros projets)
# from arrera_tk import *
```

## Détails des méthodes 

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
*   **aImage** : Widget pour afficher des images, avec support pour les thèmes clair et sombre.

### Conteneurs (Frames)

*   **aFrame** : Conteneur simple avec coins arrondis.
*   **aScrollableFrame** : Conteneur avec défilement.
*   **aCanvas** : Zone de dessin.
*   **aBackgroundImage** : Conteneur avec une image en arrière-plan.

### Fenêtres

*   **aTk** : Fenêtre principale de l'application. Gère le thème et l'icône.
*   **aTopLevel** : Fenêtre secondaire.
*   **windows_about** : Fenêtre "À propos" pré-configurée.

### Utilitaires

*   **keyboad_manager** : Utilitaire pour gérer les événements clavier (associer des fonctions à des touches).

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