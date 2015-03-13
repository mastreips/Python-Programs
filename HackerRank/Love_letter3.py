#!/usr/bin/env python

def mixer(a):
    for i in range(0,len(a)-1):
        j=0
        k=0
        while j < k :
            while a[j] != a[i]:
                if a[i] > a[j]:
                    a[i]= a[i]-1
                else:
                    a[j] = a[j]-1
                k += 1
            i -= 1
            j += 1
    return k 

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        a = str(input())
        res = mixer(a)
        print(res)