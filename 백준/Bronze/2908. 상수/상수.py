numbers = list(input().split())
reverse_num = []
for n in numbers:
    n = n[::-1]
    reverse_num.append(int(n))

print(max(reverse_num))
    