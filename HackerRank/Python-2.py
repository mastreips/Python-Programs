#!/usr/bin/env python

#!/usr/bin/env python
N = input()
k = input()
lists= [input() for _ in range(0,N)]
lists.sort()
diff_arr = [i + k - 1 - i for i in range(len(lists) - (k - 1))]
print(diff_arr)
#print min(diff_arr)

