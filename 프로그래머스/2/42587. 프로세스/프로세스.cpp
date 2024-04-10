#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int,int>> q;
    int size = priorities.size();
    
    for(int i = 0; i < size; i++)
       q.push({i,priorities[i]});

    sort(priorities.begin(),priorities.end(),greater<>()); // 우선순위 높은 순서대로 정렬
    int i = 0;
    while(!q.empty()){
        pair<int,int> procoess = q.front();
        q.pop();
        if(procoess.second == priorities[i]){
            answer++; 
            i++;

            if(procoess.first == location)
                break;
        }else
            q.push(procoess);
    }
    return answer;
}