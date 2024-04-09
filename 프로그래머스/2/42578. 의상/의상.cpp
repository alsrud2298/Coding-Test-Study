
#include <string>
#include <vector>
#include <unordered_map>
// 서로 다른 옷의 조합 수, 하루에 최소 한개
// type별 가짓수를 계산하고 총 경우의 수를 반환한다.
using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_map<string,int> m;

    for(auto cloth: clothes){
        m[cloth[1]]++; // cloth[1] = 의상 종류
    }

    // 조합 계산
    int answer = 1;

    for(auto pair: m)
        answer *= (pair.second + 1);

    return answer -1; // 아무것도 안입은 경우 제외
}
