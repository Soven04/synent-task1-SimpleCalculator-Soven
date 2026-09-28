# Command-Line Calculator

A simple **command-line calculator built using Python** that performs basic arithmetic operations through user input.

## Features

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Takes input directly from the user
* Handles invalid numerical inputs
* Handles invalid operators
* Prevents division by zero
* Displays the calculated result in the terminal

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

1. Make sure Python is installed on your system.
2. Save the program as:

```text
calculator.py
```

3. Open a terminal in the project directory.
4. Run:

```bash
python calculator.py
```

## Usage

The program asks you to enter:

1. First number
2. Arithmetic operation
3. Second number

### Example

```text
=== Command-Line Calculator ===
Enter first number: 10
Enter operation (+, -, *, /): *
Enter second number: 5
Result: 50.0
```

## Error Handling

The calculator handles common invalid inputs.

### Invalid Number

```text
Enter first number: abc
Error: Please enter valid numbers.
```

### Invalid Operator

```text
Enter operation (+, -, *, /): %
Error: Invalid operation.
```

### Division by Zero

```text
Enter first number: 10
Enter operation (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero.
```

## Project Structure

```text
calculator/
│
├── calculator.py
└── README.md
```

## Technologies Used

* **Python 3**
* Command Line / Terminal
