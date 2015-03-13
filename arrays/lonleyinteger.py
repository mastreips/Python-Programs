#!/usr/bin/env python

# Head ends here
def lonelyinteger(b):
    answer = 0
    count = 0
    for i in b:
        for j in b:
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