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
    
#######
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


#######
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

