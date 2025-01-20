
import pytest
from main import factorial

def test_factorial_zero():
    """Test factorial of 0"""
    assert factorial(0) == 1

def test_factorial_one():
    """Test factorial of 1"""
    assert factorial(1) == 1

def test_factorial_negative():
    """Test factorial of negative number"""
    assert factorial(-10) == 1

def test_factorial_string():
    """Test factorial of a string"""
    assert factorial("Hello World") == 1
