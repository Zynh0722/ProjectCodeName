import pytest
from trackmanagementsystem.main_page_funcs import black_delorean, red_ford, blue_toyota


def test_travis_1():
    assert (True is True)


def test_delorean_1():
    assert (black_delorean() is True)


def test_red_ford_1():
    assert (red_ford() is True)


def test_blue_toyota_1():
    assert  (blue_toyota() is True)
