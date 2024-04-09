#include<string>
#include<vector>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    vector<char> v;
    
    for(int i = 0; i < s.size(); i++){
        if(s[i]==')'){ //닫는 괄호가 나왔을 때,
            if(v.size() >= 1 && v.back()=='('){ //stack 바닥에 여는 괄호가 있으면
                v.pop_back(); // 짝 완성했으므로 pop
            }else{
                return false; // 남아있는 여는 괄호가 없을 경우
            }
        } else
            v.push_back(s[i]); // 여는 괄호는  stack에 담기
    }
    
    // 다 진행했는데 여는 괄호가 남은 경우 false
    return v.empty() ? true : false;
}