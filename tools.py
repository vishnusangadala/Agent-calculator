# tools.py
import re
from typing import List
from langchain_core.tools import tool

_number_re = re.compile(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?")

def _two_nums(text: str) -> List[float]:
    """Extract two numbers from free-form text like '3, 100' or '3 minus 100'."""
    nums = [float(x) for x in _number_re.findall(text)]
    if len(nums) < 2:
        raise ValueError("Please provide at least two numbers, e.g., '3 and 100'.")
    return nums[:2]

@tool
def echo(text: str) -> str:
    """Echo back the provided text."""
    return text

@tool
def add(text: str) -> str:
    """Add two numbers. Accepts free-form input like 'add 3 and 5' or '3, 5'."""
    a, b = _two_nums(text)
    return str(a + b)

@tool
def subtract(text: str) -> str:
    """Subtract the second number from the first. Input like '3 minus 100' or '3, 100'."""
    a, b = _two_nums(text)
    return str(a - b)

@tool
def multiply(text: str) -> str:
    """Multiply two numbers. Input like '12 * 3' or '12 and 3'."""
    a, b = _two_nums(text)
    return str(a * b)

@tool
def divide(text: str) -> str:
    """Divide the first number by the second. Input like '8 / 2' or '8, 2'."""
    a, b = _two_nums(text)
    if b == 0:
        return "Error: Division by zero"
    return str(a / b)

@tool
def power(text: str) -> str:
    """Compute a^b. Input like '2^8', '2 to the power 8', or '2, 8'."""
    a, b = _two_nums(text)
    return str(a ** b)

TOOLS = [echo, add, subtract, multiply, divide, power]
