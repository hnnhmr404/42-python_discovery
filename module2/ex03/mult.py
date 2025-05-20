#!/usr/bin/env python3

a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))

product = a * b

print(f"{a} x {b} = {product}")

if product > 0:
    print("The result is positive.")
elif product < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
