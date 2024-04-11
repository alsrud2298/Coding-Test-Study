#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int i = 0, j = 0;
    int size = brown + yellow;
    for(int i = 3; i <= size/2; i++){
        j = size / i;
        
        if((i-2)*(j-2) == yellow){
            answer.push_back(i);
            answer.push_back(j);
            break;
        }
    }
    int temp;
    if(answer[0] < answer[1]){
        temp = answer[0];
        answer[0] = answer[1];
        answer[1] = temp;
    }
        
    return answer;
}