from sympy import Symbol, floor, nan, oo, E, symbols, ceiling, pi, Rational, \
        Float, I, sin, exp, log, factorial

from sympy.utilities.pytest import XFAIL


def test_floor():

    x = Symbol('x')
    y = Symbol('y', real=True)
    k, n = symbols('k,n', integer=True)

    assert floor(nan) == nan

    assert floor(oo) == oo
    assert floor(-oo) == -oo

    assert floor(0) == 0

    assert floor(1) == 1
    assert floor(-1) == -1

    assert floor(E) == 2
    assert floor(-E) == -3

    assert floor(2*E) == 5
    assert floor(-2*E) == -6

    assert floor(pi) == 3
    assert floor(-pi) == -4

    assert floor(Rational(1, 2)) == 0
    assert floor(-Rational(1, 2)) == -1

    assert floor(Rational(7, 3)) == 2
    assert floor(-Rational(7, 3)) == -3

    assert floor(Float(17.0)) == 17
    assert floor(-Float(17.0)) == -17

    assert floor(Float(7.69)) == 7
    assert floor(-Float(7.69)) == -8

    assert floor(I) == I
    assert floor(-I) == -I

    assert floor(oo*I) == oo*I
    assert floor(-oo*I) == -oo*I

    assert floor(2*I) == 2*I
    assert floor(-2*I) == -2*I

    assert floor(I/2) == 0
    assert floor(-I/2) == -I

    assert floor(E + 17) == 19
    assert floor(pi + 2) == 5

    assert floor(E + pi) == floor(E + pi)
    assert floor(I + pi) == floor(I + pi)

    assert floor(floor(pi)) == 3
    assert floor(floor(y)) == floor(y)
    assert floor(floor(x)) == floor(floor(x))

    assert floor(x) == floor(x)
    assert floor(2*x) == floor(2*x)
    assert floor(k*x) == floor(k*x)

    assert floor(k) == k
    assert floor(2*k) == 2*k
    assert floor(k*n) == k*n

    assert floor(k/2) == floor(k/2)

    assert floor(x + y) == floor(x + y)

    assert floor(x + 3) == floor(x + 3)
    assert floor(x + k) == floor(x + k)

    assert floor(y + 3) == floor(y) + 3
    assert floor(y + k) == floor(y) + k

    assert floor(3 + I*y + pi) == 6 + floor(y)*I

    assert floor(k + n) == k + n

    assert floor(x*I) == floor(x*I)
    assert floor(k*I) == k*I

    assert floor(Rational(23, 10) - E*I) == 2 - 3*I

    assert floor(sin(1)) == 0
    assert floor(sin(-1)) == -1

    assert floor(exp(2)) == 7

    assert floor(log(8)/log(2)) != 2
    assert int(floor(log(8)/log(2)).evalf(chop=True)) == 3

    assert floor(factorial(50)/exp(1)) == \
        11188719610782480504630258070757734324011354208865721592720336800


def test_ceiling():

    x = Symbol('x')
    y = Symbol('y', real=True)
    k, n = symbols('k,n', integer=True)

    assert ceiling(nan) == nan

    assert ceiling(oo) == oo
    assert ceiling(-oo) == -oo

    assert ceiling(0) == 0

    assert ceiling(1) == 1
    assert ceiling(-1) == -1

    assert ceiling(E) == 3
    assert ceiling(-E) == -2

    assert ceiling(2*E) == 6
    assert ceiling(-2*E) == -5

    assert ceiling(pi) == 4
    assert ceiling(-pi) == -3

    assert ceiling(Rational(1, 2)) == 1
    assert ceiling(-Rational(1, 2)) == 0

    assert ceiling(Rational(7, 3)) == 3
    assert ceiling(-Rational(7, 3)) == -2

    assert ceiling(Float(17.0)) == 17
    assert ceiling(-Float(17.0)) == -17

    assert ceiling(Float(7.69)) == 8
    assert ceiling(-Float(7.69)) == -7

    assert ceiling(I) == I
    assert ceiling(-I) == -I

    assert ceiling(oo*I) == oo*I
    assert ceiling(-oo*I) == -oo*I

    assert ceiling(2*I) == 2*I
    assert ceiling(-2*I) == -2*I

    assert ceiling(I/2) == I
    assert ceiling(-I/2) == 0

    assert ceiling(E + 17) == 20
    assert ceiling(pi + 2) == 6

    assert ceiling(E + pi) == ceiling(E + pi)
    assert ceiling(I + pi) == ceiling(I + pi)

    assert ceiling(ceiling(pi)) == 4
    assert ceiling(ceiling(y)) == ceiling(y)
    assert ceiling(ceiling(x)) == ceiling(ceiling(x))

    assert ceiling(x) == ceiling(x)
    assert ceiling(2*x) == ceiling(2*x)
    assert ceiling(k*x) == ceiling(k*x)

    assert ceiling(k) == k
    assert ceiling(2*k) == 2*k
    assert ceiling(k*n) == k*n

    assert ceiling(k/2) == ceiling(k/2)

    assert ceiling(x + y) == ceiling(x + y)

    assert ceiling(x + 3) == ceiling(x + 3)
    assert ceiling(x + k) == ceiling(x + k)

    assert ceiling(y + 3) == ceiling(y) + 3
    assert ceiling(y + k) == ceiling(y) + k

    assert ceiling(3 + pi + y*I) == 7 + ceiling(y)*I

    assert ceiling(k + n) == k + n

    assert ceiling(x*I) == ceiling(x*I)
    assert ceiling(k*I) == k*I

    assert ceiling(Rational(23, 10) - E*I) == 3 - 2*I

    assert ceiling(sin(1)) == 1
    assert ceiling(sin(-1)) == 0

    assert ceiling(exp(2)) == 8

    assert ceiling(-log(8)/log(2)) != -2
    assert int(ceiling(-log(8)/log(2)).evalf(chop=True)) == -3

    assert ceiling(factorial(50)/exp(1)) == \
        11188719610782480504630258070757734324011354208865721592720336801


def test_series():
    x, y = symbols('x,y')
    assert floor(x).nseries(x, y, 100) == floor(y)
    assert ceiling(x).nseries(x, y, 100) == ceiling(y)
    assert floor(x).nseries(x, pi, 100) == 3
    assert ceiling(x).nseries(x, pi, 100) == 4
    assert floor(x).nseries(x, 0, 100) == 0
    assert ceiling(x).nseries(x, 0, 100) == 1
    assert floor(-x).nseries(x, 0, 100) == -1
    assert ceiling(-x).nseries(x, 0, 100) == 0


@XFAIL
def test_issue_1050():
    assert floor(3 + pi*I + y*I) == 3 + floor(pi + y)*I
    assert floor(3*I + pi*I + y*I) == floor(3 + pi + y)*I
    assert floor(3 + E + pi*I + y*I) == 5 + floor(pi + y)*I
