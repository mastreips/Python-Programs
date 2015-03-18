n,m = [int(x) for x in input().split()]
ops = list()
ans= 0
ans_avg = 0
[ops.append(input()) for _ in range(m)]

for i in range(m):
    a,b,k = ops[i].split()
    ans += (int(b)-int(a)+1)*int(k) # the position doesn't matter, just the amount!!
    ans_avg = (ans/n)
print(int(ans_avg))