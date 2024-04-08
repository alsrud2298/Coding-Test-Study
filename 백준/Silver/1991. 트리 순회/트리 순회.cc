#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// 전위 순회 : 루트 -> 왼쪽 -> 오른쪽
// 중위 순회 : 왼쪽 -> 루트 -> 오른쪽
// 후위 순회 : 왼쪽 -> 오른쪽 -> 루트

static int n; // 노드 개수
static int tree[26][2];
void preOrder(int now);
void inOrder(int now);
void postOrder(int now);

int main(){

    cin >> n;

    for(int i = 0; i < n; i++){
        char node_char, left, right;

        cin >> node_char >> left >> right;
        
        int node = node_char - 'A'; // 노드를 인덱스로 바꾸기 

        if (left == '.'){
            tree[node][0] = -1;
        }
        else{
            tree[node][0] = left - 'A';
        }

        if (right == '.'){
            tree[node][1] = -1;
        }
        else{
            tree[node][1] = right - 'A';
        }
    }

    preOrder(0);
    cout << "\n";
    inOrder(0);
    cout << "\n";
    postOrder(0);
    cout << "\n";
}

void preOrder(int now){
    if(now == -1) return;
    cout << (char)(now + 'A'); // 현재
    preOrder(tree[now][0]); // 왼쪽
    preOrder(tree[now][1]); // 오른쪽
}
void inOrder(int now){
    if(now == -1) return;
    inOrder(tree[now][0]); // 왼쪽
    cout << (char)(now + 'A'); // 현재
    inOrder(tree[now][1]); // 오른쪽

}
void postOrder(int now){
    if(now == -1) return;
    postOrder(tree[now][0]); // 왼쪽
    postOrder(tree[now][1]); // 오른쪽
    cout << (char)(now + 'A'); // 현재
}