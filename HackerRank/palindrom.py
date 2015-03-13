#!/usr/bin/env python

def checker(a):
    rev = a[::-1]
   
    if a == rev:
        return True
    else:
        return False
            
def mixer(a):
    return checker(a)

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        a = str(input())
        res = checker(a)
        print(res)