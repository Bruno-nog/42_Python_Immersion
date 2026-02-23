from typing import Any

def add(a: int, b: int) -> int:
    """add two variables"""
    return a + b

def subtract(a: int, b: int) -> int:
    """subtract two variables"""
    return a - b

def divide(a: int, b: int) -> float:
    """divide two variables"""
    if (b == 0):
        raise ValueError("Cannot divide by zero")
    else:
        return a / b

def multiply(a: int, b: int) -> int:
    """multiply two variables"""
    return a * b

def power(base: int, exponent: int) -> Any:
    """operates two variables"""
    return base ** exponent