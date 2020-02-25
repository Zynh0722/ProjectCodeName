import toga
import trackmanagementsystem.main_page_funcs as main_page_funcs
from toga.style.pack import Pack, COLUMN, ROW

drivers = []
vehicles = []

left_queue = []
right_queue = []


def red_ford_handler(widget):
    main_page_funcs.red_ford()


def blue_toyota_handler(widget):
    main_page_funcs.blue_toyota()


def black_delorean_handler(widget):
    main_page_funcs.black_delorean()


def send_to_queue_handler(widget, row):
    print()
    print(row)
    # main_page_funcs.send_to_queue(vehicles[row], right_queue)


def build(app):
    table_container = toga.Table(headings=["Make/model", "Year", "Color", "Engine", "Name", "Sponsors", "Club"],
                                 data=vehicles, style=Pack(width=300, alignment="right", padding=30),
                                 on_select=send_to_queue_handler)

    def load_vehicles_handler(widget):
        # print(main_page_funcs.load_drivers_from_json("drivers.json")[0].__dict__.values())
        loaded_vehicles = [list(obj.__dict__.values()) for obj in
                           main_page_funcs.load_vehicles_from_json("vehicles.json")]
        string_vehicles = []
        for vehicle in loaded_vehicles:
            string_vehicles.append([str(entry) for entry in vehicle])
        # print(string_drivers)
        table_container.data = string_vehicles

    load_vehicles_command = toga.Command(load_vehicles_handler, label="load vehicles",
                                         tooltip="load the vehicles from the json save file")

    racing_label = toga.Label("Currently Racing")

    racing_content = toga.Box(style=Pack(direction=ROW, padding=50))

    left_racing = toga.Button("vroom", on_press=black_delorean_handler,
                              style=Pack(width=100, padding=20))
    racing_content.add(left_racing)
    right_racing = toga.Button("zoom", on_press=black_delorean_handler,
                               style=Pack(width=100, padding=20))
    racing_content.add(right_racing)

    queued_label = toga.Label("Currently Queued")

    queued_content = toga.Box(style=Pack(direction=ROW, padding=50))
    left_queued = toga.Button("nyoom", on_press=black_delorean_handler,
                              style=Pack(width=100, padding=20))
    queued_content.add(left_queued)
    right_queued = toga.Button("fwoom", on_press=black_delorean_handler,
                               style=Pack(width=100, padding=20))
    queued_content.add(right_queued)

    left_content = toga.Box(style=Pack(direction=COLUMN, padding_top=50))

    left_content.add(racing_label)
    left_content.add(racing_content)
    left_content.add(queued_label)
    left_content.add(queued_content)

    # mid_content = toga.Box(style=Pack(direction=COLUMN, padding_top=50))
    #
    # mid_content.add(toga.Button("Hello there.", on_press=black_delorean_handler, style=Pack(width=200, padding=20)))
    #
    # mid_container = toga.ScrollContainer(horizontal=False)
    #
    # mid_container.content = mid_content
    #
    # left_content = toga.Box(
    #     style=Pack(direction=COLUMN, padding_top=50)
    # )
    #
    # for b in range(0, 10):
    #     left_content.add(
    #         toga.Button(
    #             'Red Ford %s' % b,
    #             on_press=red_ford_handler,
    #             style=Pack(width=200, padding=20)
    #         )
    #     )

    right_container = toga.ScrollContainer(horizontal=True)

    right_container.content = left_content

    split = toga.SplitContainer()

    split.content = [right_container, table_container]

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

    app.main_window.toolbar.add(load_vehicles_command)

    return split


def main():
    return toga.App('Track Management System', 'org.beeware.helloworld', startup=build, author="<ProjectCodeName>")
