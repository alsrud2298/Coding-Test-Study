def solution(arr):
    from math import gcd # 최대공약수 구하는 함수 import
    answer = arr[0] # answer을 arr[0]으로 초기화
    #1. (arr[0],arr[1])의 최소공배수를 구한 후 answer에 저장
    #2. (#1에서 구한 최소공배수, arr[2])의 최소공배수를 구한 후 answer에 저장
    #3. 모든 배열을 돌면서 최소공배수를 구하고, 저장하고 하는 방식을 진행
    for num in arr:
        answer = answer * num // gcd(answer,num)
    return answer