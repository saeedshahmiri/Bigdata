import pytest

# test_addition.py

def add(x, y):

    return x + y

def test_addition():
  
    # Define test inputs
    num1 = 5
    num2 = 7
    expected_result = 12
    

    actual_result = add(num1, num2)
    
    
    assert actual_result == expected_result, f"Addition failed: {num1} + {num2} = {actual_result}"
