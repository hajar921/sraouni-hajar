# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a-b 


def multiply(a: Number, b: Number) -> Number:
   return a*b


def divide(a: Number, b: Number) -> Number:
     if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
