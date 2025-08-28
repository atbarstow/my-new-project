"""
main.py

This file contains basic functions for the 'my-new-project' repository.
"""


def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def square(number):
    """Return the square of a number."""
    return number * number


def main():
    """Main function to run the program."""
    user_name = input("Enter your name: ")
    print(greet(user_name))


if __name__ == "__main__":
    main()
