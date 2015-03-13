N = int(input())
K = int(input())
lists = [int(input()) for _ in range(0,N)]

lists.sort()
#print(lists)

def minUF(n, k, list1):
    length = len(list1)
    subset = list()
    store = list()
    temp = pow(10,9)
    i=0
    #for i in range(0, length):
    #for i in range(0,length, k):
    for i in range(0,length-k):
        subset = list1[i:(i+k)]
        min1 = min(subset)
        max1 = max(subset)
        if min1 != max1: #and list1.count(min1) < 2: #this is working for double number e.g. 571
            fair = max1 - min1
        else:
            fair = min1
        if fair < temp:
            temp = fair
            store = fair
        #print(subset)
        #print(i,k)

    return store

min_diff = minUF(N, K, lists)

print(min_diff)