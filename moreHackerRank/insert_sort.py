#!/usr/bin/env python


n = int(input()) #size of the array
list1 = raw_input().split() #works on some not others. weird thing about raw_input()
list1 = list(map(int, list1))
insert_here = None
print(list1)
V = list1[n-1]
for i in range(n-2):
    print(list1[i])
    if list1[i]==V:
        insert_here = i
    list1[i+1] = list1[i]
    print(list1)
    
    list1[insert_here] = V
print(list1)