import winreg


def get_windows_theme_mode():
    try:
        # Ouvre la clé de registre
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        )
        # Lit la valeur "AppsUseLightTheme"
        value, _ = winreg.QueryValueEx(registry_key, "AppsUseLightTheme")
        winreg.CloseKey(registry_key)

        # Si la valeur est 1, c'est le mode clair, sinon sombre
        return "light" if value == 1 else "dark"
    except FileNotFoundError:
        return "unknown"  # Cas où la clé de registre n'existe pas
    except Exception as e:
        return f"error: {e}"


# Exemple d'utilisation
theme_mode = get_windows_theme_mode()
print(f"Le mode Windows actuel est : {theme_mode}")
