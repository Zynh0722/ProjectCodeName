import toga
import trackmanagementsystem.main_page_funcs as main_page_funcs
from toga.style.pack import Pack, COLUMN


def red_ford_handler(widget):
    main_page_funcs.red_ford()


def blue_toyota_handler(widget):
    main_page_funcs.blue_toyota()


def black_delorean_handler(widget):
    main_page_funcs.black_delorean()


def build(app):

    data = [
        ('root%s' % i, 'value %s' % i)
        for i in range(1, 100)
    ]

    left_container = toga.Table(headings=['Red Ford', 'Value'], data=data)

    right_content = toga.Box(
        style=Pack(direction=COLUMN, padding_top=50)
    )

    for b in range(0, 10):
        right_content.add(
            toga.Button(
                'Red Ford %s' % b,
                on_press=red_ford_handler,
                style=Pack(width=200, padding=20)
            )
        )
    right_container = toga.ScrollContainer(horizontal=False)

    right_container.content = right_content

    split = toga.SplitContainer()

    split.content = [left_container, right_container]

    # red_ford_button = toga.Button('Red Ford', on_press=red_ford_handler)
    # red_ford_button.style.padding = 50
    # red_ford_button.style.flex = 1
    # box.add(red_ford_button)
    #
    # blue_toyota_button = toga.Button('Blue Toyota', on_press=blue_toyota_handler)
    # blue_toyota_button.style.flex = 1
    # blue_toyota_button.style.padding = 50
    # box.add(blue_toyota_button)
    #
    # black_delorean_button = toga.Button('Black DeLorean', on_press=black_delorean_handler)
    # black_delorean_button.style.padding = 50
    # black_delorean_button.style.flex = 1
    # box.add(black_delorean_button)

    return split


def main():
    return toga.App('First App', 'org.beeware.helloworld', startup=build)
