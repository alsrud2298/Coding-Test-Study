#include<vector>
#include<queue>
#include<string.h>
using namespace std;
bool visited[104][104]; // 방문여부
int dist[104][104]; // 거리
int dx[4] = {1,-1,0,0}; // 방향
int dy[4] = {0,0,1,-1}; // 방향
queue<pair<int,int>> q;

int solution(vector<vector<int> > maps)
{   
    int answer = 0;
    int n = maps.size();
    int m = maps[0].size();
    memset(dist,-1,sizeof(dist)); // -1로 초기화
    q.push({0,0});
    visited[0][0] = 1;
    dist[0][0] = 1;
    
    while(!q.empty()){
        auto cur = q.front(); q.pop();
        // 종료조건
        if(cur.first == n -1 && cur.second == m -1){
            return dist[n-1][m-1];
        }
        for(int dir = 0; dir < 4; dir++){
            int nx = cur.second + dx[dir];
            int ny = cur.first + dy[dir];
            if(nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
            if(visited[ny][nx] || maps[ny][nx] == 0 || dist[ny][nx] != -1) continue;
            q.push({ny,nx});
            visited[ny][nx];
            dist[ny][nx] = dist[cur.first][cur.second] + 1 ;
        }
    }
    if(dist[n-1][m-1] == -1) return -1;
    else return dist[n-1][m-1];
}