import pytest
import sys
sys.path.append("..")
from exercice1 import Calculator

calculator = Calculator()

def test_add():
    result = calculator.add(2, 3)
    assert result == 5
    assert calculator.get_memory() == 5

def test_subtract():
    result = calculator.subtract(5, 2)
    assert result == 3
    assert calculator.get_memory() == 3

def test_multiply():
    result = calculator.multiply(4, 5)
    assert result == 20
    assert calculator.get_memory() == 20

def test_divide():
    result = calculator.divide(10, 2)
    assert result == 5
    assert calculator.get_memory() == 5

    with pytest.raises(ValueError):
        calculator.divide(10, 0)

def test_power():
    result = calculator.power(2, 3)
    assert result == 8
    assert calculator.get_memory() == 8

def test_sqrt():
    result = calculator.sqrt(25)
    assert result == 5
    assert calculator.get_memory() == 5

    with pytest.raises(ValueError):
        calculator.sqrt(-25)

def test_clear_memory():
    calculator.clear_memory()
    assert calculator.get_memory() == 0

if __name__ == "__main__":
    pytest.main()
