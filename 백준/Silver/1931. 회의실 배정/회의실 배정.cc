#include <iostream>
#include <vector>
#include <algorithm>



using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    
    vector<pair<int,int>> A(N);

    for(int i = 0; i < N; i++){ // 종료 시간이 우선순위가 높음 (정렬할 때)
        cin >> A[i].second; // 시작
        cin >> A[i].first; // 종료
    }

    sort(A.begin(), A.end());

    int count = 0;
    int end = -1;

    for(int i = 0; i < N; i++){
        if(A[i].second >= end){ // 시작시간이 종료시간 이후라면
            end = A[i].first; // 종료시간 업데이트 
            count ++;
        }
    }

    cout << count << endl;
}