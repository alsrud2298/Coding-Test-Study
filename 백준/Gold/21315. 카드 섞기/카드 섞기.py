import math
import sys
input = sys.stdin.readline

n = int(input())
after = list(map(int,input().split()))

def shuffle(cardlist, index):
    if index == 0:
        return cardlist
    divide_cardlist = cardlist[len(cardlist) - index:] # N - 2^(k)
    return shuffle(divide_cardlist, index//2) + cardlist[:len(cardlist) - index]

result = [] 
M = int(math.log2(n)) # k^2 < N 

for k1 in range(1, M+1): # K 최대값까지
    for k2 in range(1, M+1):
        card_list = [i for i in range(1,n+1)]
        if shuffle(shuffle(card_list, 2**k1), 2**k2) == after:
            result.append((k1,k2))

print(*result[0])