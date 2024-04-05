#include <iostream>
#include <string>

using namespace std;
// 대문자,소문자 변환 toupper(), tolower()
// 아스키코드 숫자 48-57, 대문자 65-90, 소문자 97-122
int main(void) {
    string str;
    cin >> str;
    
    int i = 0;
    /* 문자열 반복 아래와 같은 방식으로 가능
    for (char const &c: s) {
        std::cout << c << ' ';
    }
    */
    
   for(char ch: str){
        if (islower(ch))
            cout << (char)toupper(ch);
        else
            cout << (char)tolower(ch);
        i++;
    }
    
    return 0;
}