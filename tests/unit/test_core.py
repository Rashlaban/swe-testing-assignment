import pytest
from quick_calc.core import add, subtract, multiply, divide, DivisionByZeroError


def test_add_integers():
    assert add(5, 3) == 8


def test_subtract_integers():
    assert subtract(10, 4) == 6


def test_multiply_integers():
    assert multiply(6, 7) == 42


def test_divide_integers():
    assert divide(8, 2) == 4


def test_divide_by_zero_raises():
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)


def test_add_negative_numbers():
    assert add(-5, -3) == -8


def test_multiply_decimals():
    assert multiply(2.5, 4) == 10.0


def test_large_number_addition():
    assert add(10**12, 10**12) == 2 * 10**12