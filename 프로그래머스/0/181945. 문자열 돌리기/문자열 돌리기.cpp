#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    
    for(const auto ch: str) // auto 키워드 : 변수의 자료형을 컴파일 시간에 자동으로 추론
        cout << ch << endl;
    return 0;
}