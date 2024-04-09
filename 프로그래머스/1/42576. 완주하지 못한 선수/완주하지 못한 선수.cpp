#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string,int> m;
    // player count하기
    for(auto player : participant)
        if(m.end() == m.find(player))
            m.insert(make_pair(player,1));
        else
            m[player]++;
    
    //완주한 사람 --
    for(auto player: completion)
        m[player]--;
    
    // 완주하지 못한 사람 찾기
    for(auto player: participant)
        if(m[player] > 0) // 완주 못했으면
        {
            answer = player;
            break;
        }
    
    return answer;
}