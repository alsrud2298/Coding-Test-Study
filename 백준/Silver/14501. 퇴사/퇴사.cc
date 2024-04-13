// 경로 탐색
#include<iostream>
#include<vector>
#include<cstring>
#include<unordered_map>
using namespace std;

int res[16];
int cost[16];
int day[16];
int n;

void DP(){
    int deadline;
    for(int i = n; i > 0; i--){
        deadline = i + day[i];
        if(deadline > n+1){ // 마감일 = 퇴사일 이후라면 
            res[i] = res[i+1]; //상담불가, 이전값 그대로 이동
        }
        else
            // 상담 가능, 최대 이익 판별
            res[i] = max(res[i+1],res[deadline]+ cost[i]);
    }
}

int main(){
    
    cin >> n;

    for(int i = 1; i <= n; i++){
        cin >> day[i] >> cost[i];
    }

    DP();

    cout << res[1];
    return 0;
}