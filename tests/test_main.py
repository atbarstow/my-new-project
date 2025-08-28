"""
test_main.py

Unit tests for main.py functions.
"""

from main import greet, square


def test_greet_basic():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_greet_empty():
    assert greet("") == "Hello, !"


def test_square_positive():
    assert square(2) == 4
    assert square(5) == 25


def test_square_zero():
    assert square(0) == 0


def test_square_negative():
    assert square(-3) == 9
