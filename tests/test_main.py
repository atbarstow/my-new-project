"""
test_main.py

Unit tests for main.py functions.
"""

from main import greet


def test_greet_basic():
    """Test greet() returns correct greeting."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_greet_empty():
    """Test greet() with empty string."""
    assert greet("") == "Hello, !"


def test_greet_numbers():
    """Test greet() with numbers as input."""
    assert greet("123") == "Hello, 123!"
