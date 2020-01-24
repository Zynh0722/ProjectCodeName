import pytest
import trackmanagementsystem.app as app
import trackmanagementsystem.main_page_funcs as main_funcs


def test_travis_1():
    assert (True is True)

def test_hello_there_1():
    assert (main_funcs.hello_there() == True)
