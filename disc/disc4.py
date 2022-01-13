def count_stair_ways(n):
    if n == 0:
        return 0
    elif n ==1:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n, k):
    if n == 0:
        return 1
    elif k == 1:
        return 1
    elif n <0:
        return 0
    else:
        result = 0
        i = 1
        while k >= i:
            result += count_k(n-i, k)
            i += 1
        return result

def even_weighted(x):
    i = 0
    y =[]
    for i in range(len(x)):
        if i % 2 == 0:
            y.append(x[i] * i) 
    return y

def max_product(s):
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))