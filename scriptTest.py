import subprocess
from gi.repository import Gio


def is_dark_mode_enabled():
    """
    Vérifie si le mode sombre est activé sous GNOME
    Retourne: bool - True si le mode sombre est activé, False sinon
    """
    try:
        # Accès aux paramètres via GSettings
        settings = Gio.Settings.new('org.gnome.desktop.interface')
        color_scheme = settings.get_string('color-scheme')

        # Vérification de la valeur
        if color_scheme == 'prefer-dark':
            return True
        else:
            return False

    except Exception as e:
        print(f"Erreur lors de la vérification du mode sombre: {e}")
        return None


def main():
    dark_mode = is_dark_mode_enabled()
    if dark_mode is True:
        print("Le mode sombre est activé")
    elif dark_mode is False:
        print("Le mode sombre est désactivé")
    else:
        print("Impossible de déterminer l'état du mode sombre")


if __name__ == "__main__":
    main()