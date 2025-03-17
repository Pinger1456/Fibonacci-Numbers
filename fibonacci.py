"""Module to calculate Fibonacci numbers."""


def calculate_fibonacci(nth):
    """Calculate and display the Nth Fibonacci number."""
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        return
    if nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        return

    second_to_last_number = 0
    last_number = 1
    fib_numbers_calculated = 2
    print('0, 1, ', end='')  # Display the first two Fibonacci numbers.

    while True:
        next_number = second_to_last_number + last_number
        fib_numbers_calculated += 1

        print(next_number, end='')

        if fib_numbers_calculated == nth:
            print()
            print()
            print(f'The #{fib_numbers_calculated} Fibonacci'
                  f'number is {next_number}')
            break

        print(', ', end='')

        second_to_last_number = last_number
        last_number = next_number


def display_warning():
    """Display a warning for large numbers."""
    print('WARNING: This will take a while to display on the')
    print('screen. If you want to quit this program before it is')
    print('done, press Ctrl-C.')
    input('Press Enter to begin...')
