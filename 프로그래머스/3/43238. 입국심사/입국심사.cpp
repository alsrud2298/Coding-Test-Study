#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    // 가장 큰 값 뽑기 위해 정렬
    sort(times.begin(), times.end());
    
    long long min = 1;
    
    long long max = n*(long long)times.back();
    
    // 이분 탐색
    // 최대값과 최소값이 바뀌는 구간이 가장 최소 시간임
    while(min <= max){
    
    long long mid = max - (max - min)/2;
    long long tmp = 0;
        
    // 현재 시간 기준 심사위원들이 몇명 처리하는지?
    for(int i = 0; i < times.size(); i++){
        tmp+= (mid / (long long) times[i]);
    }
    // 현재보다 더 많은 사람 처리할 수 있는 경우
    if(tmp >= n){
        max = mid - 1; // 최대 시간 줄이기
        answer = mid;
    }
    else min = mid + 1;  // 최소 시간 늘리기
    }
    
    return answer;
}