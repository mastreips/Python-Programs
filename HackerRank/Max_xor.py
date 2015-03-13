#!/usr/bin/python3
def maxXor(l, r):
  
  high = 0
 
  
  for i in range(l,r+1):
    #print(i)
    for j in range(l,r+1):
      #print(j)
      test = i^j
      #print(test)
      if test > high:
        high = test
  
  return high


if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))