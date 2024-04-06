#include <iostream>
#include <vector>
#include <algorithm> // 정렬
using namespace std;

int main()
{
    // 입출력 속도 단축 효과
    ios::sync_with_stdio(false); // C++ 표준 스트림 동기화 비활성화
    cin.tie(NULL); // 내부적으로 ccin, cout 묶어주는 과정 수행하지 않으므로 시간 절약
    cout.tie(NULL);

    int N;
    cin >> N;
    vector<int> A(N,0); // 사이즈 : N, 0으로 초기화

    // 입력 받기
    for(int i = 0; i < N; i++){
        cin >> A[i]; 
    }

    // 1. 정렬
    sort(A.begin(), A.end());

    // 2. 좋은 수 개수 구하기
    int Result = 0;

    for(int k = 0; k < N; k++){
        long find = A[k]; // 판별해야하는 수
        int i = 0;
        int j = N-1;

        while(i<j){
            if(A[i] + A[j] == find){
                if(i != k && j != k ){
                    Result++;
                    break;
                }
                else if(i == k){ // 자기자신은 포함시키면 안됨
                    i++;
                }
                else if(j==k){
                    j--;
                }
            }
            else if(A[i] + A[j] < find){
                i++;
            }   
            else if(A[i] + A[j] > find){
                j--;
            }

        }
        

    }
    cout << Result << endl;
}
