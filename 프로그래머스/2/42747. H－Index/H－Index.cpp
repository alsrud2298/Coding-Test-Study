#include <string>
#include <vector>
#include <algorithm>

using namespace std;
// h번 이상 인용된 논문이 h편 이상인 경우, h의 최대값
// size - 해당 인덱스 = h-index
int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(),citations.end());
    int size = citations.size();
    
    for(int i = 0; i < size; i++){
        int h_index = size - i;
        // h편 이상 인용된 논문이 h번 이상인 경우
        if(citations[i] >= h_index)
            return h_index;
    }
    return answer;
}