def wears_jacket_with_if(temp, raining):
    if(temp < 60 or raining == True):
        return True
    else:
        return False

def square(x):
    print("here")
    return  x * x
def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0
def is_prime(n):
    i = 2
    while(i < n/2):
        if(n % i == 0):
            return False
        i = i + 1
    return True
    # if n == 1:
    #     return False
    # for x in range(2, n):
    #     if n % x == 0:
    #         return False
    # return True