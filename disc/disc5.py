def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
        return [label] + list(branches)
# Selectors
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
# For convenience
def is_leaf(tree):
    return not branches(tree)

def height(t):
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])

def max_path_sum(t):
    if is_leaf(t):
        return label(t)
    else:
        return max([max_path_sum(b) for b in branches(t)]) + label(t)

def square_tree(t):
    # if is_leaf(t):
    #     return tree(label(t) ** 2)
    # else:
        return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])

def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    else:
        paths = [find_path(b, x) for b in branches(tree)]
        for path in paths:
            if path:
                return [label(tree)] + path

def count_nodes(t):
    return 1 + sum([count_nodes(b) for b in branches(t)])

def list_leaves(t):
    if is_leaf(t):
        return [label(t)]
    else:
        leaves = []
        for b in branches(t):
            leaves += list_leaves(b)
        return leaves
        # return sum([list_leaves(b) for b in branches(t)], [])

def print_tree(t, indent=0):
    if(is_leaf(t)):
        print('  ' * indent + str(label(t)))
        print(label(t))
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

# ref:https://guohangma.herokuapp.com/2018/10/08/cs61a-disc04/



