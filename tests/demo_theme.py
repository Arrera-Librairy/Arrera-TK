from tests.demo import *


def main():
    print("Theme possible :")
    for theme in list_theme:
        print(f"- {theme}")
    theme = input("Theme : ")
    if theme not in list_theme:
        theme = "defaut"
    demo = arreratk_demo(theme=theme)
    demo.view()

if __name__ == "__main__":
    main()

