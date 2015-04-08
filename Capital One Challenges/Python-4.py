#!/usr/bin/env python
from itertools import groupby
import string
list1 = []

list1 = raw_input().lower()
list1 = list1.strip().split()
list1 = [''.join(c for c in s if c not in string.punctuation) for s in list1]


output = [list(set(list(group))) for key,group in groupby(sorted(list1,key=sorted),sorted)]
for x in range(len(output)):
    if len(output[x]) > 1:
        print(' '.join(output[x]))
    else:
        pass

