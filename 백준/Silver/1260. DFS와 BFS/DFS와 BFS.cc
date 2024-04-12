#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>
using namespace std;

const int MAX = 1002;
int N,M,V;
bool visited[MAX];
vector<int> arr[MAX];
queue<int> q;

void dfs(int now){
    visited[now] = true;
    cout << now << " ";

    for(int i = 0; i < arr[now].size(); i++){
        int next = arr[now][i];
        if(!visited[next]){
            dfs(next);
        }
    }
}

void bfs(int temp){
    q.push(temp);
    visited[temp] = true;

    while(!q.empty()){
        int x = q.front();
        q.pop();
        cout << x << " ";

        for(int i = 0; i < arr[x].size(); i++){
            int next = arr[x][i];
            if(!visited[next]){
                q.push(next);
                visited[next] = true;
            }
        }
    }
}


int main(){
    
    cin >> N >> M >> V;
    int u,v;

    for(int i = 0; i < M; i++){
        cin >> u >> v;
        // 무방향이므로
        arr[u].push_back(v);
        arr[v].push_back(u);
    }

    for(int i = 1; i <= N; i++){
        sort(arr[i].begin(), arr[i].end());
    }

    dfs(V);
    cout << endl;
    memset(visited, false, sizeof(visited));
    bfs(V);
}