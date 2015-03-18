t = int(input())
ops = list()
import math
[ops.append(input()) for _ in range(t)]

for i in range(t):
    n,c,m = ops[i].split()
    t = math.floor((int(m) * math.floor(int(n)/int(c)) - 1) / (int(m) - 1))
    print(int(t))
