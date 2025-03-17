"""Main module to run the Fibonacci sequence program."""

import sys
from fibonacci import calculate_fibonacci, display_warning


def main():
    """Main function to handle user input and display Fibonacci numbers."""
    print('''Fibonacci Sequence, by Al Sweigart al@inventwithpython.com

The Fibonacci sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
''')

    while True:  # Main program loop.
        while True:  # Keep asking until the user enters valid input.
            print('Enter the Nth Fibonacci number you wish to')
            print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
            response = input('> ').upper()

            if response == 'QUIT':
                print('Thanks for playing!')
                sys.exit()

            if response.isdecimal() and int(response) != 0:
                nth = int(response)
                break  # Exit the loop when the user enters a valid number.

            print('Please enter a number greater than 0, or QUIT.')
        print()

        if nth >= 10000:
            display_warning()

        calculate_fibonacci(nth)


if __name__ == "__main__":
    main()
