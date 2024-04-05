#include <iostream>

using namespace std;
// 이스케이프 문자 출력 -> 원시 문자열 리터럴
// R"(출력원하는 문자열)";
int main(void) {
    cout << R"(!@#$%^&*(\'"<>?:;)";
    return 0;
}