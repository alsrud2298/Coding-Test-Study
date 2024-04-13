#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N,M;
int box[1001][1001]; // 그래프 & 일 수 저장
int dy[4] = {1,-1,0,0};
int dx[4] = {0,0,1,-1};

queue <pair<int,int>> q; // 익은 토마토 위치 저장

// 박스 내부에 있는지 
bool is_inside(int ny, int nx){
    return (ny >= 0 && ny < N && nx >= 0 && nx < M);
}

void bfs(){
    
    while(!q.empty()){
        auto cur = q.front(); q.pop();

        for(int i = 0; i < 4; i++){
            int ny = cur.first + dy[i];
            int nx = cur.second + dx[i];

            if(is_inside(ny,nx) && box[ny][nx]==0 ){
                box[ny][nx] = box[cur.first][cur.second] + 1;
                q.push({ny,nx});
            }
        }
    }
}

int main(){
    
    cin >> M >> N ;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin >> box[i][j];
            // 익은 토마토 위치 저장
            if(box[i][j]==1)
                q.push({i,j});
        }

    }

    bfs();

    // 최대 일 수 찾기
    int max = 0;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            // 안 익은 토마토가 남아있는 경우
            if(box[i][j] == 0){
                cout << -1 << '\n';
                return 0;
            }
            if(max < box[i][j])
                max = box[i][j]; // 최대 값 찾기
        }
    }

    cout << max - 1 << '\n'; //시작일이 1일이므로
    return 0;
}