#include <iostream>
#include <vector>

using namespace std;

static vector<vector <int>> A;
static vector<bool> visited;
static bool arrive;

void dfs(int now, int depth);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M ;
    // 초기값 선언
    arrive = false; // depth 5까지 도착했는지 아닌지 
    cin >> N >> M;
    A.resize(N); // A vector 크기 N만큼 resize
    visited = vector<bool>(N, false); // false로 초기화

    // 그래프 데이터 저장

    for (int i = 0; i < M; i++){
        int s, e;
        cin >> s >> e;
        // 양방향으로 저쟝해줘야 함.
        A[s].push_back(e); // vector의 끝에 요소 저장. {1,3} 이런식으로 이차원 배열도 넣을 수 있음.
        A[e].push_back(s);
    }

    // 노드마다 DFS 실행
    for (int i = 0; i < N; i++)
    {
        dfs(i,1); // 1 -> depth
        if (arrive) break;
    }
    
    if(arrive){
        cout << 1 << "\n";
    }else{
        cout << 0 << "\n";
    }
        }

    
    void dfs(int now, int depth){
        // 종료 설정
        if(depth == 5 || arrive){
            arrive = true;
            return;
        }
        // 방문 처리
        visited[now] = true;
        // A[now]에 연결되어있는 모든 노드 탐색
        for(int i : A[now]){
            if(!visited[i]) dfs(i,depth+1);
        }
        visited[now] = false; // 더이상 다음으로 갈 수 없을 때, 다시 뒤로 빠져나와야함.
    }