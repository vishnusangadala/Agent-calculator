# tools.py
import re
from typing import List
from pathlib import Path
from dotenv import dotenv_values
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# --- Utility: extract two numbers from text ---
_number_re = re.compile(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?")

def _two_nums(text: str) -> List[float]:
    """Extract two numbers from free-form text like '3, 100' or '3 minus 100'."""
    nums = [float(x) for x in _number_re.findall(text)]
    if len(nums) < 2:
        raise ValueError("Please provide at least two numbers, e.g., '3 and 100'.")
    return nums[:2]

# --- Math Tools ---
@tool
def add(text: str) -> str:
    """Add two numbers. Accepts free-form input like 'add 3 and 5' or '3, 5'."""
    a, b = _two_nums(text)
    return f"The result of adding {a} and {b} is {a + b}."

@tool
def subtract(text: str) -> str:
    """Subtract the second number from the first. Input like '3 minus 100'."""
    a, b = _two_nums(text)
    return f"The result of subtracting {b} from {a} is {a - b}."

@tool
def multiply(text: str) -> str:
    """Multiply two numbers. Input like '12 * 3' or '12 and 3'."""
    a, b = _two_nums(text)
    return f"The result of multiplying {a} and {b} is {a * b}."

@tool
def divide(text: str) -> str:
    """Divide the first number by the second. Input like '8 / 2' or '8, 2'."""
    a, b = _two_nums(text)
    if b == 0:
        return "Error: Division by zero."
    return f"The result of dividing {a} by {b} is {a / b}."

@tool
def power(text: str) -> str:
    """Compute a^b. Input like '2^8', '2 to the power 8', or '2, 8'."""
    a, b = _two_nums(text)
    return f"The result of {a} raised to the power of {b} is {a ** b}."

# --- Open-Ended LLM Tool ---
@tool
def llm_response(text: str) -> str:
    """Use the language model directly for open-ended or creative questions."""
    cfg = dotenv_values(Path(__file__).parent / ".env")
    api_key = cfg.get("OPENAI_API_KEY")
    if not api_key:
        return "Error: OPENAI_API_KEY not found in .env file."

    llm = ChatOpenAI(model="gpt-4o", temperature=0.8, api_key=api_key)
    return llm.invoke(text).content

# --- Export tools ---
TOOLS = [add, subtract, multiply, divide, power, llm_response]
