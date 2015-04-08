
a, b = raw_input().split()
a = int(a)
b = int(b)

lists = [int(raw_input(), 2) for _ in range(a)]
#diff_arr = [lists[i] | lists[i+1] for i in range(len(lists)-1)]
#diff_arr = [lists[i + k - 1] - lists[i] for i in range(len(lists) - (k - 1))]
# store = list()
# for i in range(a):
#     for j in range(a):
#         bit = lists[i] | lists[j]
#         store.append(bit)
#         # if bit == bin(b):
#         #    store.append([lists[i], lists[j]])
# print(store)
# ma_x = max(diff_arr)
# bit = bin(ma_x)[2:]
# print(bit.count('1'))
# print(diff_arr.count(ma_x))
# 
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

# store = [max(combs[i]) for i in range(len(combs))]
     
#print(bit)

# 5 topics = 11111 = 31
# 4 topics = 1111 = 15
# 3 topics etc. 