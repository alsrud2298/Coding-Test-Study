# 2  3  5  9  17  33
#  +1 +2 +4 +8 +16

# (2 + 2^0 + 2^1 + 2^2 + ... + 2^(N-1))^2

N = int(input())
result = 2

for i in range(N):
    result += 2**i

print(result**2)