#include <iostream>
#include <vector>
#include <algorithm> //sort 들어있음
#include <queue>
#include <string.h> //memset 들어있음

using namespace std;

vector<int> vec[1002];
vector<int> result_dfs;
vector<int> result_bfs;
bool visit[1002]; //방문 여부: 정점에다가 표시

void dfs(int x) {
	visit[x] = true;
	result_dfs.push_back(x);

	for (int i = 0; i < vec[x].size(); i++) {
		if (!visit[vec[x][i]]) { //간선의 의미를 잘 보자.. 
			dfs(vec[x][i]);
		}
	}
}

void bfs(int temp) {
	queue<int> q;
	q.push(temp);
	visit[temp] = true;
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		result_bfs.push_back(x);

		for (int i = 0; i < vec[x].size(); i++) {
			if (!visit[vec[x][i]]) {
				q.push(vec[x][i]);
				visit[vec[x][i]] = true;
			}
		}
	}
}

int main(void) {
	int n, m, v, a, b;
	cin >> n >> m >> v;

	for (int i = 1; i <= m; i++) {
		cin >> a >> b;
		vec[a].push_back(b);
		vec[b].push_back(a); //양방향 간선처리
	}

	
	//sort해야함. 왼쪽부터 순서대로라고 생각하기 때문. 왼쪽은 작은 숫자고.
	//sort안하려면 matrix쓰고 왼쪽에서 오른쪽으로 탐색해야함. 
	for (int i = 1; i <= n; i++) {
		sort(vec[i].begin(), vec[i].end()); //벡터 안에서 sort
	}

	dfs(v);
	for (int i = 0; i < result_dfs.size(); i++) {    //정점 개수니까 n으로 for문 돌려도 되지 않을까?
		                             //안됨. 간선이 없는 경우 정점을 모두 탐색하지 않을수도 있음
		cout << result_dfs[i] << ' ';
	}
	cout << endl;

	memset(visit, false, 1002);

	bfs(v);
	for (int i = 0; i < result_bfs.size(); i++) {
		cout << result_bfs[i] << ' ';
	}

	return 0;
}