#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {

    int size = clothes.size();
    unordered_map <string, int> map; // 의상 종류, 개수
    
    for(auto cloth: clothes){
        map[cloth[1]] ++;
    }
    int answer = 1;

    for(auto pair: map)
        answer *= (pair.second+1);
    
    
    return answer - 1;
}