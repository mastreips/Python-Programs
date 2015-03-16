#!/usr/bin/env python

from itertools import combinations
import sys

i = 0
n = input()
list1 = list()
list2 = list()
while i <= n*2-1:
    list1.append(sys.stdin.readline().strip())
    i += 1
#print(list1)


def findsubsets(S,m):
    return list(combinations(S,m))

def gcd(a,b):
    while a:
        a, b = b%a, a
    return b

if len(list1) > 2:
    for j in range(0,(n*2-1),2):
        list2.append(list1[j+1])
     
        if list(reduce(lambda x,y: gcd([x,y]), list2)).__contains__('1') == True:
            print("YES")
        else:
            print("NO")

        del list2[:]
