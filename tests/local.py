from objects.driver import Driver
from objects.vehicle import Vehicle
from trackmanagementsystem.main_page_funcs import save_info_to_json, load_drivers_from_json, load_vehicles_from_json

list_of_drivers = []

driver1 = Driver("Marty McFly", "9303 Lyon Drive", "Hill Valley", "CA", 95420, 9168423138,
                 "marty.mcfly@protonmail.com")

driver2 = Driver("ur mom", "no u", "loserville", "USA", 69420, 5038675309,
                 "wakawkaakakakakakakka")

list_of_drivers.append(driver1)
list_of_drivers.append(driver2)

save_info_to_json(list_of_drivers, "drivers.json")
read_list_of_drivers = load_drivers_from_json("drivers.json")
print(read_list_of_drivers)

list_of_vehicles = []

vehicle1 = Vehicle("DeLorean", 1985, "Space grey", "Flux capacitor", "Timey Wimey",
                   "Amblin Entertainment", "Time Travelers Anonymous")

vehicle2 = Vehicle("Honda Civic", 2001, "yoda green", "pure spite", "Yoda's weapon", "The Jedi Order", "The Council")

list_of_vehicles.append(vehicle1)
list_of_vehicles.append(vehicle2)

save_info_to_json(list_of_vehicles, "../trackmanagementsystem/vehicles.json")
read_list_of_vehicles = load_vehicles_from_json("../trackmanagementsystem/vehicles.json")
