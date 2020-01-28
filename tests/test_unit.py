import pytest
import trackmanagementsystem.app as app
import objects.vehicle


def test_travis_1():
    assert (True is True)


def test_new_vehicle():
    vehicle_test = objects.Vehicle("DeLorean", 1985, "Space grey", "Flux capacity", "Timey Wimey",
                                   "Amblin Entertainment")
    assert (vehicle_test.name == "Timey Wimey")
