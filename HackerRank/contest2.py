
a, b = raw_input().split()
a = int(a)
b = int(b)

lists = [int(raw_input(), 2) for _ in range(a)]

from itertools import combinations
diff_arr = list()
combs = list((combinations(lists, 2)))
print(combs)
for i in range(len(combs)):
    (c,d)= combs[i]
    diff_arr.append(c|d)
print(diff_arr)
ma_x = max(diff_arr)
bit = bin(ma_x)[2:]
print(bit.count('1'))
print(diff_arr.count(ma_x))