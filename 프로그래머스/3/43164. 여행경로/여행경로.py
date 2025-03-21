def solution(tickets):
    for ticket in tickets:
        ticket.append(0)                                 #visited
    length = len(tickets)+1                              #경로길이
    tickets.sort(key = lambda x:x[1])                    #티켓sort
    t = ["ICN"]                                          #경로저장리스트
    def dfs(port):                                       #깊이우선탐색
        for ticket in tickets:               
            if ticket[0] == port and ticket[2] == 0:     #ticket이 루트에 해당하면서, 방문하지 않은경우
                t.append(ticket[1])                      #경로 저장
                ticket[2] = 1                            #visited 체크
                if length == len(t) or dfs(ticket[1]):   #경로가 꽉찼으면 return t 해주고, 그렇지 않으면 다음탐색
                    return t
                ticket[2] = 0                            #탐색했는데 경로 안꽉찼으면 visited = 0으로 수정 후
                t.pop()                                  #경로 빼내기
    answer = dfs("ICN")

    return answer