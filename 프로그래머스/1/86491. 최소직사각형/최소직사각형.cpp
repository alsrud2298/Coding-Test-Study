#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int w = 0;
    int h = 0;
    for(auto num: sizes){
        w = max(w,max(num[0],num[1])); // 가로세로중 더 큰값 중 가장 큰값
        h = max(h,min(num[0],num[1])); // 더 작은 값 중 가장 큰 값
    }
    return w*h;
}