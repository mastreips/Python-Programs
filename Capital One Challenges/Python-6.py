n = int(input())

#list1 = [[(raw_input()), int(input())] for i in range(n*2)]
#list1 = [raw_input() for i in range(n*2)]
list1=[]
def getKey0(item):
    return item[0]

def getKey1(item):
    return item[1]

for i in range(n):
    #print(i)
    list1.append([raw_input(), float(input())])

low = sorted(list1, key=getKey1)
# for i in range(n):
#     if list[i][1] == list[i+1][1]:
#         i = i+2
#     else:
#         break
#     
# last = low[0:i]
last = []
k=0
i=0
#last.append(low[1][0])

# for i in range(len(low)-1):
#     for j in range(len(low)-1):
#         print(low[i][j])
#         print(low[i+1][j])
#         # if low[i][j] == low[i+1][j]:
#         #     last.extend(low[i+1])
if low[i][1] != low[i+1][1]:
    last.append(low[i+1][0])
else:
    for i in range(2, len(low)-1):
        if low[i][1] == low[i+1][1]:
            pass
        else:
            last.append(low[i][0])
            k = i
            break

for i in range(k,len(low)-1):
         # print(low[i][1])
         # print(low[i+1][1])
         if low[i][1] == low[i+1][1]:
            last.append(low[i+1][0])
            #print(last)

sortlist = (sorted(last))

for x in range(len(sortlist)):
    print(sortlist[x])