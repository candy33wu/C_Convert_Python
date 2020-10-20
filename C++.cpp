#include<iostream>
#include<algorithm>
using namespace std;
struct Node {
	int a, b, d;
	bool operator<(Node b) {
		return d < b.d;
	}
}road[200001],ch[200001];
bool small(Node a,Node b) {
	return a.d < b.d;
}
int parent[200001], T, X;
int find(int a) { return a == parent[a] ? a : (parent[a] = find(parent[a])); }//find root
void Union(int a, int b) {
	parent[find(a)] = find(b);
}
int cost(int choseNum,int t) {
	int sum = 0;
	for (int i = 0; i < choseNum; ++i) {
		sum += ch[i].d;
	}
	return sum/t+t*X;
}
void t(int choseNum) {//魔法設備等級
	int min = cost(choseNum, 1);
	int t = 1;
	for (int i = 2; i < T; ++i) {
		if (cost(choseNum, i) < min) {
			min = cost(choseNum, i);
			t = i;
		}
	}
	cout << t << endl;
}
void kruskal(int n, int m) {
	for (int i = 0; i < n; ++i)
		parent[i] = i;

	sort(road, road + m,small);
	int choseNum = 0;
	//跑超過n-1表圖有cycle，依序找出最小生成樹上的V-1條邊
	for (int i = 0, j = 0; i < m && j < n - 1; i++, j++)//i: edge,j: node
	{
		//cycle 不要(已連在一起不要)
		while (find(road[i].a) == find(road[i].b))
			i++;
		//把a tree,b tree串到一起
		Union(road[i].a, road[i].b);
		ch[choseNum] = road[i];
		choseNum++;
	}
	 t(choseNum);
	cout << choseNum << endl;
	for (int i = 0; i < choseNum; ++i) {
		cout << ch[i].a << " " << ch[i].b << endl;
	}
}
int main() {
	int islandNum, roadnum;
	cin >> islandNum >> roadnum >> T >> X;
	for (int i = 0; i < roadnum; i++)
	{
		cin >> road[i].a >> road[i].b >> road[i].d;
	}
	kruskal(islandNum, roadnum);
	
}
