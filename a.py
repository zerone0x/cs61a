def combo(a, b):
    if a ==0 or b == 0:
        return a+b
    elif a % 10 == b % 10:
        return combo(a//10, b//10) + 10*(a%10)
    else:
        return max(combo(a//10, b//10), combo(a//10, b), combo(a, b//10))

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)