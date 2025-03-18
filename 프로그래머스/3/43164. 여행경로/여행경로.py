def solution(tickets):
    answer = []
    # 출발지가 같은 티켓끼리, 도착지 기준 정렬
    tickets.sort(key = lambda x: (x[0], x[1]))
    
    def dfs(t, path):
        # 티켓을 모두 소진했다면 path 리턴
        if len(t) == 0:
            return path
        
        now = path[-1]
        valid_idx = -1
        
        # 출발지가 현재 공항인 티켓을 찾아 가장 왼쪽 티켓에서 멈춤
        for i in range(len(t)):
            if t[i][0] == now:
                valid_idx = i
                break
        # 티켓이 남아있는데 나아갈 공항이 없는 경우
        if valid_idx == -1:
            return []
    
        # 출발지가 현재 공항인 티켓을 순회하면서 dfs
        # 가장 먼저 완성된 루트가 알파벳 상 가장 앞 루트
        while t[valid_idx][0] == now:
            nxt_path = dfs(t[:valid_idx] + t[valid_idx + 1:], path + [t[valid_idx][1]])
            if nxt_path != []:
                return nxt_path
            valid_idx += 1
        return []
    return dfs(tickets, ["ICN"])