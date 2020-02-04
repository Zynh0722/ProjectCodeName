import pytest
import trackmanagementsystem.app as app
from objects.vehicle import Vehicle
from objects.driver import Driver


def test_travis_1():
    assert (True is True)


def test_new_vehicle():
    vehicle_test = Vehicle("DeLorean", 1985, "Space grey", "Flux capacitor", "Timey Wimey",
                           "Amblin Entertainment")
    assert (vehicle_test.name == "Timey Wimey" and vehicle_test.engine == "Flux capacitor")


def test_new_driver():
    driver_test = Driver("Marty McFly", "9303 Lyon Drive", "Hill Valley", "CA", 95420, 9168423138,
                         "marty.mcfly@protonmail.com")

    assert (driver_test.zip_code == 95420 and driver_test.state == "CA")
