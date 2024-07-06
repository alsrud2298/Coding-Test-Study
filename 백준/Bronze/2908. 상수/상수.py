numbers = list(input().split())
reverse_num = []
for n in numbers:
    n = n[-1] + n[1] + n[0]
    reverse_num.append(int(n))

print(max(reverse_num))
    