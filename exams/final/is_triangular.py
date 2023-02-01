def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    def gen_tris():
        res = 1
        inc = 1
        while True:
            if res == 1:
                yield res
                inc += 1
                res += inc
            else:
                inc += 1
                res += inc
                yield res
    for num in gen_tris():
        if num == k:
            return True
        if num > k:
            return False



print(is_triangular(1))
print(is_triangular(2))
print(is_triangular(10))
print(is_triangular(15))