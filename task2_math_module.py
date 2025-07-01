# Task 2: Using the Math Module for Calculations

import math

# Ask user for input
try:
    number = float(input("Enter a number: "))

    if number < 0:
        print("Square root and logarithm are not defined for negative numbers.")
    else:
        print("Square root:", math.sqrt(number))
        print("Natural logarithm (log base e):", math.log(number))

    # Sine works for any number
    print("Sine (in radians):", math.sin(number))

except ValueError:
    print("Invalid input! Please enter a valid number.")
