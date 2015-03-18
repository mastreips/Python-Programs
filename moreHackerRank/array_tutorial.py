V = int(input()) #number to be searched
n = int(input()) #size of the array
list1 = input().split()
list1 = list(map(int, list1))
print(list1)
for i in range(n):
    if list1[i] == V:
        print(i)
    else:
        pass
