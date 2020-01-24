import toga
import main_page_funcs


def button_handler(widget):
    main_page_funcs.hello_there()


def build(app):
    box = toga.Box()

    button = toga.Button('Hello there', on_press=button_handler)
    button.style.padding = 50
    button.style.flex = 1
    box.add(button)

    return box


def main():
    return toga.App('First App', 'org.beeware.helloworld', startup=build)
