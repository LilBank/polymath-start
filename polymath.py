"""Functions for polynomials.

Results may be complex numbers. In Python complex numbers are
a built-in type.  Some examples:
>>> x = 3 + 4j
>>> x.real
3.0
>>> x.imag
4.0
>>> abs(x)
5.0
>>> import cmath
>>> cmath.sqrt(-1)
1j

Requires: Python 3.9 or newer for type hints.
"""
import math, cmath

def quadratic_roots(a, b, c) -> list[float|complex]:
    """Return the roots of a quadratic polynomial
       of the form a*x^2 + b*x + c.

       :returns: array of two roots of a quadratic polynomial. 
                The values are real if roots are real, otherwise complex. 
    """
    descriminant = b*b - 4*a*c
    if descriminant > 0:
        # two real roots
        sqrt_des = math.sqrt(descriminant)
        roots = [(-b + sqrt_des)/(2*a), (-b - sqrt_des)/(2*a)]
    else:
        # two complex roots
        sqrt_des = cmath.sqrt(descriminant)  # returns complex
        roots = [(-b + sqrt_des)/(2*a), (-b - sqrt_des)/(2*a)]
    return roots

