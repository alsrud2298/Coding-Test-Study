#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// 버블 정렬

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    vector<pair<int, int>> A(N);

    for(int i = 0; i < N; i++){
        cin >> A[i].first;
        A[i].second = i;
    }
    sort(A.begin(),A.end());
    // index를 사용해서 for문이 몇번 돌았는지 파악가능!
    // 전,후 인덱스 차이 
    int MAX = 0;
    for(int i  = 0; i < N; i++){
        if(MAX < A[i].second - i) // 인덱스의 차이 = swap 개수
            MAX = A[i].second-i; // 최대 인덱스 찾기

    }
    cout << MAX + 1; //swap이 안되는 1번 더해주기
}