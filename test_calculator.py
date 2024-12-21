
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(5, 0)
        import pytest
from calculator import add, subtract, multiply, divide

def test_add():
     assert add(2, 3) == 5
     assert add(-1, 1) == 0
     assert add(0, 0) == 0

def test_subtract():
     assert subtract(5, 2) == 3
     assert subtract(10, 5) == 5
     assert subtract(0, 0) == 0

def test_multiply():
     assert multiply(3, 4) == 12
     assert multiply(5, 0) == 0
     assert multiply(-2, 3) == -6

def test_divide():
     assert divide(10, 2) == 5
     assert divide(6, 3) == 2
     assert divide(1, 1) == 1
     with pytest.raises(ValueError):
         divide(5, 0)
     with pytest.raises(ValueError):
         divide(0, 0) #проверяем, что деление нуля на ноль также вызывает исключение

def test_divide_edge_cases():
    assert divide(100, 1) == 100
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(0, 5) == 0
    assert divide(5, 2) == 2.5
    assert divide(5.0, 2.0) == 2.5
    assert divide(5, 2.0) == 2.5
    assert divide(5.0, 2) == 2.5