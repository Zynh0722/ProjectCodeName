import toga
import main_page_funcs


def hello_there_handler(widget):
    main_page_funcs.hello_there()


def build(app):
    box = toga.Box()

    hello_there_button = toga.Button('Hello there', on_press=hello_there_handler)
    hello_there_button.style.padding = 50
    hello_there_button.style.flex = 1
    box.add(hello_there_button)

    goodbye_there_button = toga.Button('Goodbye', on_press=hello_there_handler)
    goodbye_there_button.style.flex = 1
    goodbye_there_button.style.padding = 50
    box.add(goodbye_there_button)

    return box


def main():
    return toga.App('First App', 'org.beeware.helloworld', startup=build)
