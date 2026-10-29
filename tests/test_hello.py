"""
test_hello.py - Test cases for hello.py application
"""
import sys
import os

# Ensure the root directory is on the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hello import get_greeting, calculate_square

def test_get_greeting_default():
    """Test 1: Verify get_greeting with default parameter."""
    result = get_greeting()
    print(f"\n[TEST CASE 1 RESULT] get_greeting() -> '{result}'")
    assert result == "Hello, World!"

def test_get_greeting_custom():
    """Test 2: Verify get_greeting with custom parameter."""
    result = get_greeting("Alice")
    assert result == "Hello, Alice!"

def test_calculate_square():
    """Test 3: Verify calculate_square calculation."""
    assert calculate_square(5) == 25
