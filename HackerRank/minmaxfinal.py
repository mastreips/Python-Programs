#!/usr/bin/env python
N = input()
k = input()
lists= [input() for _ in range(0,N)]
lists.sort()
diff_arr = [lists[i + k - 1] - lists[i] for i in range(len(lists) - (k - 1))] #this is a GENERATOR EXPRESSION
print(diff_arr)
print min(diff_arr)