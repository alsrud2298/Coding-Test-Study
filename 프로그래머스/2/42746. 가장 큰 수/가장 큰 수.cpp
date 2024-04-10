#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const string x, const string y){
    // 7,31 -> 731 > 371 이므로 731 반환
    // 3,30 -> 330 > 303
    return x+y > y+x;
}

string solution(vector<int> numbers) {
    string answer = "";

    vector<string> temp;
    for(auto num : numbers){
        temp.push_back(to_string(num));
    }
    
    sort(temp.begin(),temp.end(),cmp);
    
    for(auto ch: temp)
        answer += ch;
    // {0,0,0} 일 경우 000 -> 0으로 바꿔줘야함
    if(answer[0] == '0'){
        answer = '0';   
    }
    return answer;
}