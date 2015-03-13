#!/usr/bin/env python

def checker(a):
 
    rev = a[::-1]
   
    if a == rev:
        return True
    else:
        return False
            
def mixer(b):
    
    str1 = list(b)
    count = 0
    if checker(b) == True:
        return count
    elif str1[0] <= str1[len(str1)-1]:
        for ch in range(len(b)-1, 0, -1):
            while str1[ch] != "a":
                tag = str1[ch]
                str1[ch] = chr(ord(tag)-1)
                print(str1)
                count += 1
                if checker(str1) == True:
                    return count
    else:
        for ch in range(0,len(b)-1):
            while str1[ch] != "a":
                tag = str1[ch]
                str1[ch] = chr(ord(tag)-1)
                print(str1)
                count += 1
                if checker(str1) == True:
                    return count
    return count            

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        a = str(input())
        res = mixer(a)
        print(res)