#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string overwrite_string, int s) {

    // 문자열 크기 string.size()
    // for(int i = 0; i < overwrite_string.size(); i++){
    //     my_string[i+s] = overwrite_string[i];
    // }
    // replace 사용
    string answer = "";
    answer = my_string.replace(s,overwrite_string.size(),overwrite_string);
    
    return answer;
}