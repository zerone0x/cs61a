from black import Line
from numpy import empty


class A():
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return self.x
    def __str__(self):
        return self.x * 2
class B():
    def __init__(self):
        print("boo!")
        self.a = []
    def add_a(self, a):
        self.a.append(a)
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret
    
def sum_nums(link):
    sum = 0
    while link is not Link.empty:
        sum += link.first
        link = link.rest
    return sum


def multipy_links(lst_of_lnks):
    res = 1
    for link in lst_of_lnks:
        if link == Link.empty:
            return Link.empty
        res *= link.first
    rest_link = [link.rest for link in lst_of_lnks]
    return Link(res, multipy_links(rest_link))
    
if link is Link.empty:
    print('This linked list is empty!')
else:
    print('This linked list is not empty!')
    
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
def __repr__(self):
    if self.rest:
        rest_str = ', ' + repr(self.rest)
    else:
        rest_str = ''
    return 'Link({0}{1})'.format(repr(self.first), rest_str)
def __str__(self):
    string = '<'
    while self.rest is not Link.empty:
        string += str(self.first) + ' '
        self = self.rest
    return string + str(self.first) + '>'
# 2.3
def flip_two(lnk):
    while lnk is not Link.empty:
        lnk.first = lnk.rest.first
        lnk = lnk.rest.rest
        
        
def filter_link(link, f):
    while link is not Link.empty:
        try:
            if f(link.first):
                yield link.first
            link = link.rest
        except StopIteration:
            print("StopIteration")
    
    
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches
    
def make_even(t):
    # 简单计算条件的长return语句
    # return Tree(t.label**2, [make_even(b) for b in t.branches])
    
    # 啰嗦的solution
    # if t.is_leaf():
    #     return
    # elif t.label % 2 != 0:
    #     t.label = t.label + 1
    # for b in t.branches:
    #     if b.label % 2 != 0:
    #         b.label = b.label + 1
    #     make_even(b)
    
    # 简单的solution
    if t.lable % 2 != 0:
        t.label = t.label + 1
    for b in t.branches:
        make_even(b)



def find_path(t, entry):
    if t.label == entry:
        return [t.label]
    for b in t.branches:
        path = find_path(b, entry)
        if path:
            return path + [t.label]
        
        
def combine_tree(t1, t2, combiner):
    # 遍历两棵树的同时 create new tree 
    # if t1.is_leaf():
    #     return Tree[combiner(t1.label, t2.label)]
    # else:
    return Tree(combiner(t1.label, t2.label), [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)])
    
def alt_tree_map(t, map_fn):
    return Tree(map_fn(t.label), [alt_tree_map(b, map_fn) for b in t.branches])