# https://docs.python.org/3/library/itertools.html#itertools.permutations
import itertools
def permutations1(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

n = int(input())
k = int(input())
list = [x for x in range(1,n+1)]
beauty_list = []
beauty = 0

for i in itertools.permutations(list):
    sum = 0
    sum_list = [x for x in i]
    mult = 1
    j = 0
    while mult <= n:
        sum = sum + sum_list[j] * mult
        mult = mult + 1
        j = j + 1
    beauty_list.append(sum)

for i in beauty_list:
    if i % k == 0:
        beauty = beauty + 1

print(beauty)