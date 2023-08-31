import math

# Basic arithmetic operations
result = 2 + 3 * 4 / 2 - 1
print(result)  # Output: 9.0

# Exponentiation
result = 2 ** 3
print(result)  # Output: 8

# Modulo
result = 10 % 3
print(result)  # Output: 1

# Square root
result = math.sqrt(16)
print(result)  # Output: 4.0

# Trigonometric functions
result = math.sin(math.pi / 2)
print(result)  # Output: 1.0

import math

pi = math.pi
print(pi)  # Output: 3.141592653589793

import mpmath

mpmath.mp.dps = 50  # Set the number of decimal places
pi = mpmath.pi
print(pi)  # Output: 3.1415926535897932384626433832795028841971693993751

import mpmath

mpmath.mp.dps = 1000  # Set the number of decimal places
pi = mpmath.pi
print(pi)
