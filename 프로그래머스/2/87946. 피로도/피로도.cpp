#include <string>
#include <vector>

using namespace std;

int res;
bool visited[9];

int dfs(vector<vector<int>> dungeons, int k, int cnt){
    res = max(res,cnt); // 최대 던전수
    
    for(int i = 0; i < dungeons.size(); i++){
        // 방문할 수 없거나 최소 필요 피로도 > 현재 피로도
        if(visited[i] || dungeons[i][0] > k)
            continue;
        
        visited[i] = 1; // 방문처리
        dfs(dungeons, k-dungeons[i][1], cnt+1);
        visited[i] = 0;
    }
    return res;
}


int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    
    answer = dfs(dungeons, k, 0);
    
    return answer;
}