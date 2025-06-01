#!/usr/bin/env python3
"""
Test script for Kannadafy obfuscation.
This script contains various Python features to test the obfuscation process.
"""

def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def list_comprehension_example():
    """Demonstrate list comprehension."""
    return [x**2 for x in range(10) if x % 2 == 0]

class TestClass:
    """A simple class to test obfuscation with classes."""

    def __init__(self, name):
        self.name = name
        self.value = 0

    def increment(self, amount=1):
        """Increment the value by the given amount."""
        self.value += amount
        return self.value

    def __str__(self):
        return f"TestClass(name='{self.name}', value={self.value})"

def main():
    """Main function to demonstrate the functionality."""
    # Simple calculations
    print("Testing Kannadafy obfuscation...")

    # Calculate Fibonacci
    fib_num = calculate_fibonacci(10)
    print(f"Fibonacci(10) = {fib_num}")

    # List comprehension
    even_squares = list_comprehension_example()
    print(f"Even squares: {even_squares}")

    # Class usage
    test_obj = TestClass("test_object")
    test_obj.increment(5)
    print(test_obj)

    print("Test script executed successfully!")

if __name__ == "__main__":
    main()
