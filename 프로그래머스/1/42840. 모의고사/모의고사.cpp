#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> one = {1,2,3,4,5};
    vector<int> two = {2,1,2,3,2,4,2,5};
    vector<int> three = {3,3,1,1,2,2,4,4,5,5};
    
    int a = 0, b = 0, c = 0;
    
    for(int i = 0; i < answers.size(); i++){
        if(answers[i] == one[i % 5]) a++;
        if(answers[i] == two[i % 8]) b++;
        if(answers[i] == three[i % 10]) c++;    
    }
    int max_n = max({a,b,c});
    
    if(max_n==a) answer.push_back(1);
    if(max_n==b) answer.push_back(2);
    if(max_n==c) answer.push_back(3);
    
    return answer;
}