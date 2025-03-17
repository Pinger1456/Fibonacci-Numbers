# Fibonacci Sequence Project

This project calculates Fibonacci numbers. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The program prompts the user to enter the position of the Fibonacci number they want to calculate and then displays the result.

## Installation

1. Ensure you have Python 3.x installed. If not, download and install it from the [official website](https://www.python.org/).

2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fibonacci_project.git
   ```

3. Navigate to the project directory:
   ```bash
   cd fibonacci_project
   ```

4. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

## Usage

Run the program:
```bash
python main.py
```

The program will prompt you to enter the position of the Fibonacci number you want to calculate. Enter the number and press Enter. To exit the program, type `QUIT`.

Example:
```
Enter the Nth Fibonacci number you wish to
calculate (such as 5, 50, 1000, 9999), or QUIT to quit:
> 10

0, 1, 1, 2, 3, 5, 8, 13, 21, 34

The #10 Fibonacci number is 34.
```

## Project Structure

```
fibonacci_project/
│
├── main.py                # Main script to run the program
├── fibonacci.py           # Logic for calculating Fibonacci numbers
├── config.py              # Configuration parameters
├── README.md              # Project documentation
└── tests/                 # Directory for tests
    └── test_fibonacci.py  # Tests for the fibonacci.py module
```

## Testing

To run the tests, use the following command:

```bash
python -m unittest tests/test_fibonacci.py
```

## Code Style Checking

To check the code style against PEP8 standards, use `flake8`:

```bash
flake8 .
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.