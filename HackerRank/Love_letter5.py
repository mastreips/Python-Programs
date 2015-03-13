#!/usr/bin/env python

def mixer(b):
    a = list(b)
    i = len(a)-1
    j=0
    k=0
    while j < i :
        while a[j] != a[i]:
            if a[i] > a[j]:
                 a[i]= chr(ord(a[i])-1)
                 print(a)
            else:
                a[j] = chr(ord(a[j])-1)
                print(a)
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