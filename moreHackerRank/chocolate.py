t = int(input())
ops = list()
import math
[ops.append(input()) for _ in range(t)]
#print(ops)

for i in range(t):
    n,c,m = ops[i].split()

    # candy = int(n)/int(c)
    # #print(candy)
    # wrappers = candy
    # #print(wrappers)
    # #trade = int(wrappers/int(m))
    # trade = (wrappers)/int(m)
    # #print(m)
    # #print(trade)
    # #candy = candy + int(trade)
    # candy = int(candy)+ int(trade)
    #t = floor((m * floor(n/c) - 1) / (m - 1))
    t = math.floor((int(m) * math.floor(int(n)/int(c)) - 1) / (int(m) - 1))
    #print(candy)

    # if int(trade) > 1:
    #     #spare = wrappers % int(m)
    #     spare = int(wrappers) % int(m)
    #     candy = int(candy)+int(spare)
    #     #candy = candy + spare
    #     print(spare)

    print(int(t))
    #print(spare)

# T = int(input())
#
# for i in range(T):
#
#     N,C,M = str(input()).split()
#     answer = 0
#     # Compute Answer
#     print(answer)




    # if int(m)/wrappers >1:
    #     candy = candy + int(int(m)/wrappers)
    #     wrappers = candy - wrappers
    #
    #
    #
    # buy = int(n)/int(c)
    # bonus = buy/int(m)
    # if bonus < 1:
    #     pass
    # else:
    #     rm = bonus % int(m)
    # bonus2 = buy/rm
    # if bonus2 < 1:
    #     pass
    # else:
    #     final_bonus = bonus2
    # ans = int(buy)+int(bonus)+int(final_bonus)
    # print(ans)
    # ans = int(n)/int(c)+(int(n)/int(c)-int(m))+(int(n)/int(m))
    # print(int(ans))
    # buy = int(n)/int(c)
    # bonus = buy/int(m)
    # spare = buy % int(m)
    #
    # ans = int(buy) + int(bonus) + int(buy/(bonus+spare))
    # print(buy), print(bonus), print(int(spare)), print(ans)
    # wrap = (int(n)/int(c))/int(m)
    # ans = int(n)/int(c) +(int(n)/int(c))/int(m)
    # print(int(ans))
#    print(n), print(c), print(m)
#     ans += (int(b)-int(a)+1)*int(k) # the position doesn't matter, just the amount!!
#     ans_avg = (ans/n)
# print(int(ans_avg))