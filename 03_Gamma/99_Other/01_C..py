import math

# Basic arithmetic operations
result = 2 + 3 * 4 / 2 - 1
print(result)  # Output: 7.0

# Exponentiation
result = 2 ** 3
print(result)  # Output: 8 (2 to the component of 3 = 8)

# Modulo
result = 10 % 3
print(result)  # Output: 1 (10 divided by 3 = 3 with a remainder of 1)

# Square root
result = math.sqrt(16)
print(result)  # Output: 4.0 (the square root of 16 = 4)

# Trigonometric functions
result = math.sin(math.pi / 2)
print(result)  # Output: 1.0 (the sine of 90 degrees = 1)

import math

pi = math.pi
print(pi)  # Output: 3.141592653589793

import mpmath

mpmath.mp.dps = 50  # Set the number of decimal places
pi = mpmath.pi
print(pi)  # Output: 3.1415926535897932384626433832795028841971693993751

import mpmath

mpmath.mp.dps = 10000  # Set the number of decimal places
pi = mpmath.pi
print(pi)

mpmath.mp.dps = 10000  # Set the number of decimal places
pi = mpmath.pi
print(pi)
def calculate_pi(iterations):
    pi_approximation = 0
    for i in range(iterations):
        term = (-1) ** i / (2 * i + 1)
        pi_approximation += term
    return 4 * pi_approximation
# Example usage:
approximation = calculate_pi(10000)
print(approximation)
