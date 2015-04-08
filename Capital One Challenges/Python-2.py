#!/usr/bin/env python
from itertools import permutations

n,m = [int(x) for x in raw_input().split()]
list1 = []
diff = n-m

for i in xrange(0,diff):
    list1.append('T')

    
for j in xrange(diff,n):
    list1.append('H')

list2 = list(permutations(list1))
list3 = (list(set(list2)))

print(len(list3))