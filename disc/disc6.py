def memory(n):
    def f(g):
        nonlocal n
        return g(n)
    return f

def mystery(p, q):
    p[1].extend(q[1])
    q[1].append(p[0])

def group_by(s, fn):
    grouped = {}
    for x in s:
        key = fn(x)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(x)
    return grouped

def add_this_many(x, el, s):
    return s + [el] * x

def filter(iterable, fn):
    # return [x for x in iterable if fn(x)]
    for x in iterable:
        if fn(x):
            yield x

def merge(a, b):
   first_a, first_b = next(a), next(b)
   while True:
        if first_a == first_b:
           yield first_a
           first_a, first_b = next(a), next(b)
        elif first_a < first_b:
            yield first_a
            first_a = next(a)
        else:
            yield first_b
            first_b = next(b)