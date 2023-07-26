'''Root-finding.

https://en.wikipedia.org/wiki/Category:Root-finding_algorithms
https://www.composingprograms.com/pages/16-higher-order-functions.html
'''

__all__ = ['approx_eq', 'improve', 'sqrt']

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

def improve(update, close, guess=1.0):
    while not close(guess):
        guess = update(guess)
    return guess

def sqrt(a, tolerance=1e-3):
    def sqrt_update(x):
        return (x + a/x) / 2
    def sqrt_close(x):
        return approx_eq(x, a/x, tolerance)
    if a < 0:
        return 1j * sqrt(-a, tolerance)
    elif a == 0:
        return 0
    else:
        return improve(sqrt_update, sqrt_close)
    
