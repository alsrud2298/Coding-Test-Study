#include <vector>
#include <set> // 중복 정렬 없애고, 자동 정렬
using namespace std;
// 최대 고를 수 있는 종류의 수 = 중복 제거 후 n/2개
int solution(vector<int> nums)
{
    set<int> tmpl;
    for(const auto& num : nums)
        tmpl.insert(num);
    return min(nums.size()/2, tmpl.size());        
  
}