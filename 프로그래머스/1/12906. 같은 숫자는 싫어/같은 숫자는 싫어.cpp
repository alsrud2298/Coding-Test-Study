#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> arr) 
{   
    vector<int> stack;
    
    stack.push_back(arr.front());
    for(auto num: arr){
        if (stack.back()!= num){
            stack.push_back(num);
        }
        else
            continue;
    }

    return stack;
}