"""Unit tests of polymath functions.

These tests use pytest. To install it: `pip install pytest`

Run tests:

>>> pytest test_polymath.py
"""
from polymath import *


def test_real_roots():
    """Correctly returns two distinct real roots."""
    result = quadratic_roots(1, -5, 4)        # = (x-1)*(x-4)
    assert len(result) == 2, "Should have exactly 2 roots"
    assert isinstance(result[0], float), "Roots should be real"
    assert isinstance(result[1], float), "Roots should be real"
    assert 1.0 in result
    assert 4.0 in result
    # same thing with negative real roots
    result = quadratic_roots(-1.0, -5.0, -4.0) # -1*(x+1)*(x+4)
    assert len(result) == 2, "Should have exactly 2 roots"
    assert -1.0 in result
    assert -4.0 in result

def test_one_root_is_zero():
    """Quadratic where one of the roots is zero."""
    result = quadratic_roots(2, -20, 0)  # 2*x*(x-10)
    assert len(result) == 2, "Should have exactly 2 roots"
    assert 0.0 in result
    assert 10.0 in result

def test_both_roots_are_zero():
    """Polynomial where both roots are zero."""
    result = quadratic_roots(8, 0, 0)
    assert len(result) == 2, "Should have exactly 2 roots"
    assert result[0] == 0
    assert result[1] == 0

def test_identical_real_roots():
    """Polynomial with identical, non-zero roots."""
    result = quadratic_roots(2, -20, 50) # same as x^2 - 10x + 25
    assert len(result) == 2, "Should have exactly 2 roots"
    assert result[0] == 5.0
    assert result[1] == 5.0
    assert isinstance(result[0], float), "roots should be real"
    assert isinstance(result[1], float), "roots should be real"

def test_complex_roots():
    """Polynomial with two complex roots."""
    result = quadratic_roots(1, 4, 20)   # x^2 + 4x + 20
    assert len(result) == 2, "Should have exactly 2 roots"
    assert (-2 + 4j) in result
    assert (-2 - 4j) in result

