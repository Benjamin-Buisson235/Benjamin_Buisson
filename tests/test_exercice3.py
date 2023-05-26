import pytest
from math import pi
import sys
sys.path.append("..")
from exercice3 import Shape, Rectangle, Circle, Square

def test_rectangle():
    rectangle = Rectangle(6, 9)
    assert rectangle.perimeter() == 30
    assert rectangle.area() == 54

def test_circle():
    circle = Circle(3)
    assert circle.area() == 28.274333882308138
    assert circle.perimeter() == 18.84955592153876

def test_square():
    square = Square(4)
    assert square.area() == 16
    assert square.perimeter() == 16

if __name__ == "__main__":
    pytest.main()