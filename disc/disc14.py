def paths(x, y):
    if x == y:
        return [[x]]
    elif x > y:
        return []
    else:
        a = paths(x + 1, y)
        b = paths(x * 2, y)
        return [[x] + subpath for subpath in a + b]
    # 在return上做处理变换
    

   
def mergesort(seq):
    if len(seq) <= 1:
        return seq
    else:
        return merge(mergesort(seq[:len(seq)//2]), mergesort(seq[len(seq)//2:]))
    

def long_path(tree, n):
    
