#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int, int>> q;
    int size = priorities.size();
    
    for(int i = 0; i < size; i ++){
        q.push({i,priorities[i]}); //인덱스와 우선순위 저장
    }
    sort(priorities.begin(),priorities.end(),greater<>()); // 우선순위 큰 순서대로 정렬
    
    int i = 0;
    while(!q.empty()){
        pair<int, int> process = q.front();
        q.pop();
        
        if(process.second == priorities[i]){ // 남은 프로세스 중 우선순위가 가장 높으면
            i++; answer++; //해당 프로세스 실행 & i++, answer++; 
            if(process.first == location) // 해당 프로세스의 인덱스가 타겟값과 같으면
                break; // 멈추기
        }
        else
            q.push(process); // 더 높은 우선순위가 있으면 다시 큐에 넣기
    }
    return answer;
}