#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    a = 0
    b = 0
    la = [a0, a1, a2]
    lb = [b0, b1, b2]
    for i in range(3):
        if la[i] > lb[i]:
            a += 1
        elif la[i] < lb[i]:
            b += 1
    print('{} {}'.format(a, b))

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
