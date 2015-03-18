n = int(input())
k = int(input())
l = [int(input()) for i in range(n)]
l.sort()
k_l = [l[p:p+k] for p in range(0, len(l)-k+1)]
ans = 999999999
for j in range(len(k_l)):
    ans = min(ans, max(k_l[j])-min(k_l[j]))
print(ans)