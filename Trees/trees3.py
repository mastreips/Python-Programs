def height(a): #N 0:60
    odd = 0
    even = 0
    final = 0
    # if n == 0:
    #     return 1
    for i in range(0,a+1):
        print(i)
        if i % 2 == 1:
            odd = even*2
            final = odd
        else:
            even = odd + 1
            final = even

    return final

print(height(4))
print(height(3))
print(height(0))
print(height(1))