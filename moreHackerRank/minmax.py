N = int(input())
K = int(input())
lists = [int(input()) for _ in range(0,N)]
lists.sort()
print(lists)

def minUF(N, K, lists):
    temp = 0
    min1 = pow(10,9)
    key = list()

    for i in lists:
        for j in lists:
            for k in lists:
                print(i,j,k)
                if i==j or j==k or i==k:
                    pass
                else:
                    temp = abs(int(i) - int(j) -int(k))/3 #abs doesn't work nor does dropping it off
                    print(temp)
                    print(min1)
                    if temp < min1:
                        min1 = temp
                        key = [i, j, k]
                        print("HIT")

    x = int((max(key)))
    y = int((min(key)))
    return (x-y)


min_diff = minUF(N, K, lists)

print(min_diff)
