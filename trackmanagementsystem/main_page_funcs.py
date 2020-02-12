import json

from objects.driver import Driver
from objects.vehicle import Vehicle


def red_ford():
    print("Red Ford")
    return True


def blue_toyota():
    print("Blue Toyota")
    return True


def black_delorean():
    print("Black DeLorean")
    return True


def save_info_to_json(list_of_objects, filename):
    with open(filename, "w+") as save_file:
        json.dump([obj.__dict__ for obj in list_of_objects], save_file)


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


def load_vehicles_from_json(filename):
    with open(filename, "r") as vehicles_file:
        json_of_vehicles = json.load(vehicles_file)
    print(type(json_of_vehicles))
    list_of_vehicles = []
    for vehicle in json_of_vehicles:
        list_of_vehicles.append(
            Vehicle(vehicle["make_model"], vehicle["year"], vehicle["color"], vehicle["engine"], vehicle["name"],
                    vehicle["sponsors"], vehicle["club"]))
    return list_of_vehicles
