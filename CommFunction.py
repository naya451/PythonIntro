from itertools import permutations

def checkcomm(fun, *args):
    perms = permutations(args)
    first_result = fun(*next(perms))
    for perm in perms:
        if fun(*perm) != first_result:
            return False
    return True
