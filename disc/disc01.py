def wears_jacket_with_if(temp, raining):
    """
    
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    if raining or temp < 60:
        return True
    else:
        return False

def wears_jacket(temp, raining):
    return raining or temp < 60

def is_prime(n):
    """
        
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return False

    k = 2
    while k < n:
        if n % k == 0:
            return False
        k = k + 1
    return True




