this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    def add(b):
        nonlocal a
        res = a + b
        a += 1
        return res
    return add

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    f1 = 0
    f2 = 1
    def fib():
        nonlocal f1, f2
        if f1 == 0 and f2 == 1:
            f1, f2 = f2, f1 + f2
            return 0
        elif f1 == 1 and f2 == 1:
            f1, f2 = f2, f1 + f2
            return 1
        else:
            res = f1
            f1, f2 = f2, f1 + f2
            return res
    return fib

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    # i = len(lst)
    # j = 0
    # while i > 0: 
    #     if lst[j] == entry:
    #         lst = lst[:j+1] + [elem] + lst[j+1:]
    #         i-=1
    #         j+=2
    #     else:
    #         i -=1
    #         j +=1
    # return lst
    # 不知错误在哪
    j = 0
    while j < len(lst): 
        if lst[j] == entry:
            lst.insert(j + 1, elem)
            if elem == entry:
                j += 1
        j +=1
    return lst