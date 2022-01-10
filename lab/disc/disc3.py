from typing import MutableMapping


def multifply(m, n):
    if n == 1:
        return m
    else:
        return multifply(m,n-1)+m
    
def hailstone(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        print(n)
        return hailstone(n // 2)
    else:
        print(n)
        return hailstone(n * 3 + 1)

'''----------------------------------------------------'''
def split(n):
    return n // 10, n % 10

def smallest(a, b):
    if(b == 0):
        return a
    elif b == 0:
        return a
    else: 
        return min(a,b)


def merge(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1%10 < n2%10:
        return merge(n1//10,n2)*10 + n1%10
    else:
        return merge(n1,n2//10)*10 + n2%10

'''----------------------------------------------------'''
def make_func_repeater(f, x):
    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return f(repeat(n-1))
    return repeat

def is_prime(n):
    if n == 1:
        return False
    k = 2
    def prime_helper(k):
        if k == n:
            return True
        elif n % k == 0:
            return False
        else:
            return prime_helper(k+1)
    return prime_helper(k)
