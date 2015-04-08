#!/usr/bin/env python

n = int(input())
list1 = []
list1 = raw_input().split() 
list1 = list(map(int, list1))


def change(n, list1, test=None):
    test = [] if test is None else test
    if n == 0:
        yield test
    for i in list1:
 
        if i > n or (len(test) > 0 and test[-1] < i):
            continue
    
        for result in change(n - i, list1=list1, test=test + [i]):
            yield result

print(len(list(change(n, list1))))
