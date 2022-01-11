HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if(x < 8):
        return 0
    elif(x % 10 == 8):
        return 1 + num_eights(x//10)
    else:
        return num_eights(x//10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def help(n):
        if(n<=7):
            return 0
        elif(num_eights(n)>0 or n % 8 == 0):
            return 1 + help(n-1)
        else:
            return help(n-1)


    if(n <= 7):
        return n
    elif(num_eights(n)>0 or n % 8 == 0):
        return pingpong(n-1)+pow(-1,help(n-1))
    else:
        return pingpong(n-1)+pow(-1,help(n))



def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    if(n < 10):
        return 0
    elif(n // 10 % 10 != n % 10 - 1 and n // 10 % 10 != n % 10):
        return  n % 10 - 1 - (n // 10 % 10) + missing_digits(n // 10)
    else:
        return missing_digits(n // 10)


def next_largest_coin(coin):
    """Return the next coin.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
'''模式很简单，但很难套用进去。比如tree一般是从最大值开始分支，如果给的是小->大，就得先递减到最大值的临界点，然后再从这递归到最小值。'''
def max(x):
    if(x <= 1):
        return 0
    else:
        i = x
        while not next_largest_coin(i):
            i-=1
        if(x < next_largest_coin(i)):
            return i
        else:
            return next_largest_coin(i)

def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def count_partitions(n, m):
        if n == 1 or n == 0:
            return 1
        elif n < 0:
            return 0
        elif m <= 0:
            return 0
        elif m == 1:
            return 1
        else:
            with_m = count_partitions(n-max(m), max(m))
            without_m = count_partitions(n, max(m-1))
            return with_m + without_m
    return count_partitions(total, max(total))





from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # return lambda n: 1 if n == 1 else mul(n, make_anonymous_factorial()(sub(n, 1)))
    return (lambda f: lambda k: f(f,k)) (lambda f,k: 1 if k == 1 else k * f(f, sub(k,1)))

""" 在lambda中写递归，需要将func本身作为func的参数传入。先定义func(func,k).再按照将函数传入"""
