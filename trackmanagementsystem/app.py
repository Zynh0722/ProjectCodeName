import toga


def button_handler(widget):
    print("hello")
    return True


def build(app):
    box = toga.Box()

    button = toga.Button('Hello world', on_press=button_handler)
    button.style.padding = 50
    button.style.flex = 1
    box.add(button)

    return box


def main():
    return toga.App('First App', 'org.beeware.helloworld', startup=build)
