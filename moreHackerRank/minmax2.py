N = int(input())
K = int(input())
lists = [int(input()) for _ in range(0,N)]

lists.sort()
print(lists)

def rec(y, k1, length, k):
    global sum
    global store
    sum = 0
    store = list()

    for i in range(y,k1):
        #print(y, k1, i)
        if i < length-1:
            sum = abs(lists[i]-lists[i+1])
            #store=sum
            #print(sum)
            y += 1
            #return sum
        else:
            pass
        store.extend([sum])
        print(len(store)), print(k)
        if len(store) == int(k):
            print(store)

def minUF(N, K, lists):
    temp = 0
    #sum = 0
    j = 1
    k1 = K
    length = len(lists)
    min1 = pow(10,9)
    y=0
    store = list()


    # for j in range(0,length-1):
    #     for i in range(y,k1):
    #         sum = abs(lists[i]-lists[i+1])
    #         print(sum)
    #         y += 1
    #         if k1+1 <= length:
    #             k1 +=1

    while j <= (length-1):
        #print(rec(y,k1, length))
        rec(y,k1, length, K)
        j +=1
        y +=1
        k1 += 1
        #store.extend([sum])

    #return store
min_diff = minUF(N, K, lists)

print(min_diff)
