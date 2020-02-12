import json

from objects.driver import Driver


def red_ford():
    print("Red Ford")
    return True


def blue_toyota():
    print("Blue Toyota")
    return True


def black_delorean():
    print("Black DeLorean")
    return True


def save_drivers_to_json(list_of_drivers):
    with open("drivers.json", "w+") as drivers_file:
        json.dump([obj.__dict__ for obj in list_of_drivers], drivers_file)


def load_drivers_from_json(filename):
    with open(filename, "r") as drivers_file:
        json_of_drivers = json.load(drivers_file)
    print(type(json_of_drivers))
    list_of_drivers = []
    for driver in json_of_drivers:
        list_of_drivers.append(
            Driver(driver["name"], driver["address"], driver["city"], driver["state"], driver["zip_code"],
                   driver["phone"], driver["email"]))
    return list_of_drivers
