def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    
    while len(progresses) > 0: 
        if (progresses[0] + day * speeds[0]) >= 100: # 작업 진도가 100 이상이면
            progresses.pop(0) # 진도 리스트에서 삭제
            speeds.pop(0) # 속도 리스트에서 삭제
            count += 1 # 배포 개수 + 1
        else:
            if count > 0: # 현재 작업 진도가 100%가 아닌데, 앞에 배포할 작업이 있었다면
                answer.append(count) # 배포개수 answer에 담은 후
                count = 0 #초기화
            day += 1 #다음 날짜 작업 확인
    answer.append(count)
    return answer