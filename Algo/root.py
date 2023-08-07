'''Root-finding.

https://en.wikipedia.org/wiki/Category:Root-finding_algorithms
https://www.composingprograms.com/pages/16-higher-order-functions.html
'''

__all__ = [
    'approx_eq',
    'improve',
    'sqrt',
    'newton_update',
    'find_zero',
    'nth_root',
]

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

def improve(update, close, guess=1.0):
    while not close(guess):
        guess = update(guess)
    return guess

def sqrt(a):
    def sqrt_update(x):
        return (x + a/x) / 2
    def sqrt_close(x):
        return approx_eq(x, a/x)
    if a < 0:
        return 1j * sqrt(-a)
    elif a == 0:
        return 0
    else:
        return improve(sqrt_update, sqrt_close)

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def close(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), close)

def nth_root(radicand, index):
    def f(x):
        return x**index - radicand
    def df(x):
        return index * x**(index-1)
    return find_zero(f, df)
    
