def height(n): #N 0:60
    odd = 2
    even = 3 #to account for 0
    if n == 0:
        return 1
    if n == 1:
        return 2
    for i in range(2,n):
        if i % 2 == 1:
            odd += 1
        else:
            even += 1

    return odd*2 + even

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        a = int(input())
        res = height(a)
        print(res)

