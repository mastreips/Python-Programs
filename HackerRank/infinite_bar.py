#!/usr/bin/env python
import math
ops = list()
T = int(input())
[ops.append(raw_input()) for _ in range(T)]

for i in xrange(T):
    a = ops[i]
    b = float(a)

    root = b/2
    if root - int(root) == 0:
        print(int(root ** 2))
    else:
        c = int(root)
        d = c+1
        print(int(c*d))

    