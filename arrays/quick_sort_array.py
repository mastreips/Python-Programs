#!/usr/bin/env python

from array import *

i_array = array('I',[55, 23, 26, 2, 25])
alist = [55, 23, 26, 2, 25]

print(i_array)
print(alist)

def partition(arr, low, high):
    pivot_value = arr[low]
    i = low
    j = high
    
    while i < j:
        if arr[i] <= pivot_value and i <= high:
            i += 1
        if arr[j] > pivot_value:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
        
    arr[low] = arr[j]
    arr[j] = pivot_value
    
    return j
    
def quick_sort_rec(a, l, h):
    if h > l:
        pivot_index = partition(a, l, h)
        quick_sort_rec(a, l, pivot_index-1)
        quick_sort_rec(a, pivot_index+1, h)
        
def quick_sort(a):
    quick_sort_rec(a, 0, len(a) - 1)

quick_sort(i_array)
print(i_array)

quick_sort(alist)
print(alist)
        