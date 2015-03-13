#!/usr/bin/env python
import math
ops = list()
count = 0
T = int(raw_input())
[ops.append(raw_input()) for _ in range(T)]

    
for i in xrange(T):
    a,b = ops[i].split()
    rB = int(math.floor(math.sqrt(float(b))))
    rA = int(math.ceil(math.sqrt(float(a))))
    print(rB-rA +1)

    