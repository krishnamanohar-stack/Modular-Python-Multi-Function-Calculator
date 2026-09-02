# Modular Python Multi-Function Calculator

A modular command-line calculator built with Python. The project combines basic calculations, scientific operations, number theory utilities, financial calculations, input validation, and calculation history into a single menu-driven application.

## Features

### Basic Calculator

* Addition
* Subtraction
* Multiplication
* Division
* Modulus

### Scientific Calculator

* Power
* Square Root
* Percentage
* Factorial
* Absolute Value
* Exponential
* Natural Logarithm
* Logarithm Base 10
* Sine
* Cosine
* Tangent
* Cube Root

### Number Theory

* GCD
* HCF
* LCM
* Prime Number Check
* Prime Factorization
* Fibonacci Number
* Fibonacci Series
* Perfect Number Check
* Divisors
* Sum of Divisors
* Armstrong Number Check

### Finance Calculator

* Simple Interest
* Compound Interest
* Discount
* Profit / Loss
* Tax
* EMI

### Additional Features

* Modular Python architecture
* Input validation
* Error handling
* Calculation history
* Clear history option
* Menu-based navigation
* Edge-case handling

## Technologies Used

* Python
* Python Standard Library
* `math`
* File handling
* Functions
* Modules
* Exception handling
* Input validation

## Project Structure

```text
calculator/
│
├── main.py
│
├── calculator_modules/
│   ├── basic.py
│   ├── scientific.py
│   ├── number_theory.py
│   ├── finance.py
│   ├── validators.py
│   ├── history.py
│   └── __init__.py
│
├── history.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project directory

```bash
cd calculator
```

### 3. Run the calculator

```bash
python main.py
```

## Input Validation

The calculator validates user input before performing calculations.

Examples include:

* Integer validation for menu choices
* Positive integer validation
* Non-negative integer validation
* Numeric validation for decimal-compatible calculations
* Validation for mathematical restrictions such as logarithms and square roots
* Protection against division by zero
* EMI validation for invalid time periods

## Calculation History

Successful calculations can be saved to `history.txt`.

The application provides options to:

1. View calculation history
2. Clear calculation history

Calculation history is intentionally excluded from version control using `.gitignore`.

## Error Handling

The calculator handles invalid inputs and mathematical errors without terminating the application.

Examples:

* Division by zero
* Modulus by zero
* Invalid menu choices
* Invalid numeric input
* Negative square-root input
* Invalid logarithm input
* Invalid factorial input
* Invalid EMI duration

## Learning Goals

This project was built to practice intermediate Python concepts including:

* Functions
* Modules and packages
* Importing custom modules
* Conditional statements
* Loops
* Input validation
* Exception handling
* File handling
* Mathematical operations
* Modular program design
* Debugging and testing

## Future Improvements

Possible future improvements include:

* GUI interface
* Unit testing with `pytest`
* Better command-line interface
* More financial calculations
* More scientific operations
* Improved result formatting
* Configuration options

## Author

**Venkata Krishna Manohar Kuraku**

Computer Science Engineering student interested in software development and backend development.
