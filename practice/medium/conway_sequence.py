from collections import deque
from itertools import groupby

r = int(input())
l = int(input())

result = deque([[r]], maxlen=2)
for _ in range(l):
    temp = []
    for i, g in groupby(result[-1]):
        temp += [len(list(g)), i]
    result.append(temp)

print(*result[0])


# Good generator solution
from itertools import groupby

r = [int(input())]
l = int(input())

def next_row(r):
    for v, lst in groupby(r):
        yield sum(1 for k in lst)
        yield v
        
for n in range(l-1):
    r = next_row(r)

print(*r)
