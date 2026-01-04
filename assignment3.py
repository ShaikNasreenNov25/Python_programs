# Task1_factorial.py

def factorial(number):
    if  number == 0:
        return 1
    else:
        return number*factorial(number-1)

number = int(input("Enter a number: "))
result = factorial(number)
print(f"Factorial of {number} is: {result}")

print("\n|============================|\n")

# Task2_math_module.py
import math
number = int(input("Enter a number: "))

print(f"Square root: {math.sqrt(number)}")

print(f"Logarithm: {math.log(number)}")

print(f"Sine: {math.sin(number)}")

print("\n|=====Code End Thankyou=====|")
