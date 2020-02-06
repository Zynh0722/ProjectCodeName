import pytest

from trackmanagementsystem.main_page_funcs import black_delorean, red_ford, blue_toyota
import trackmanagementsystem.app as app
from objects.vehicle import Vehicle
from objects.driver import Driver


def test_travis_1():
    assert (True is True)


def test_delorean_1():
    assert (black_delorean() is True)


def test_red_ford_1():
    assert (red_ford() is True)


def test_blue_toyota_1():
    assert  (blue_toyota() is True)
    
def test_new_vehicle():
    vehicle_test = Vehicle("DeLorean", 1985, "Space grey", "Flux capacitor", "Timey Wimey",
                           "Amblin Entertainment", "Time Travelers Anonymous")
    assert (vehicle_test.name == "Timey Wimey" and vehicle_test.engine == "Flux capacitor")


def test_new_driver():
    driver_test = Driver("Marty McFly", "9303 Lyon Drive", "Hill Valley", "CA", 95420, 9168423138,
                         "marty.mcfly@protonmail.com")

    assert (driver_test.zip_code == 95420 and driver_test.state == "CA")
