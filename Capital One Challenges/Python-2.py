#!/usr/bin/env python
from itertools import permutations

n,m = [int(x) for x in input().split()]
list1 = []
diff = n-m

def perma(diff):
    for i in range(0,diff):
        list1.append('T')


    for j in range(diff,n):
        list1.append('H')

    list2 = list(permutations(list1))
    list3 = (list(set(list2)))

    return(len(list3))

print(perma(diff))

import cProfile  #explore profile
cProfile.run('perma(diff)')