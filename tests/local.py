from objects.driver import Driver
from trackmanagementsystem.main_page_funcs import save_drivers_to_json, load_drivers_from_json

list_of_drivers = []

driver1 = Driver("Marty McFly", "9303 Lyon Drive", "Hill Valley", "CA", 95420, 9168423138,
                 "marty.mcfly@protonmail.com")

driver2 = Driver("ur mom", "no u", "loserville", "USA", 69420, 5038675309,
                 "wakawkaakakakakakakka")

list_of_drivers.append(driver1)
list_of_drivers.append(driver2)

save_drivers_to_json(list_of_drivers)

read_list_of_drivers = load_drivers_from_json("drivers.json")

print(read_list_of_drivers)