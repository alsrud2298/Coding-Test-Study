from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    tangerine.sort(reverse = True, key = lambda t: (counter[t],t))
    return len(set(tangerine[:k]))
