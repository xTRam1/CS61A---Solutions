"- FUNCTIONS -"

"""Question 1.1
>>> from operator import add, mul
>>> mul(add(5, 6), 8)
>>> print('x')
>>> y = print('x')
>>> print(y)
>>> print(add(4, 2), print('a'))"""

""">>> 88
>>> x
>>> x
>>> None
>>> a
>>> 6 None"""

""" Question 1.2
>>> def foo(x):
    print(x)
    return x + 1
>>> def bar(y, x):
    print(x - y)
>>> foo(3)
>>> bar(3)
>>> bar(6, 1)
>>> bar(foo(10), 11)"""

""">>> 3
>>> 4
>>> Error
>>> -5
>>> 10
>>> 0"""

" - CONTROL - "

def count_matches(n, m):
    '''
    >>> count_matches(10, 30)
    1
    >>> count_matches(12345, 23456)
    0
    >>> count_matches(121212, 123123)
    2
    >>> count_matches(111, 11) # only one's place matches
    2
    >>> count_matches(101, 10) # no place matches
    0
    '''
    count = 0
    while n != 0 or m != 0:
        first_last, second_last = n % 10, m % 10,
        if first_last == second_last:
            count += 1
        n, m = n // 10, m // 10
    return count

def count_digits(n):
    '''
    >>> count_digits(4)
    1
    >>> count_digits(12345678)
    8
    >>> count_digits(0)
    0
    '''
    count = 0
    while n != 0:
        count += 1
        n = n // 10
    return count

" - HIGHER ORDER FUNCTIONS - "

def make_skipper(n):
    """
    >>> a = make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    def f(x):
        k = 1
        while k <= x:
            if k % n != 0:
                print(k)
            k += 1
    return f

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
        ... # Even numbers have remainder 0 when divided by 2.
        ... return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    k = 1
    while k <= n:
        if cond(k):
            print(k)
        k += 1

def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
        ... # Even numbers have remainder 0 when divided by 2.
        ... return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return f
