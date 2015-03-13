#!/usr/bin/env python

# Head ends here
def lonelyinteger(b):
    answer = 0
    count = 0
    list1 = list(b)
    for i in list1:
        for j in list1:
            if i == j:
                count += 1
        if count < 2:
            answer = i
            break
        else:
            count = 0
                
    return answer        
             
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))