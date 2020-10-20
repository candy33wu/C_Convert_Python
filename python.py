from ctypes import *
import numpy as np
class Node(Structure):
    _fields_=[
        ('a', c_int32),
        ('b', c_int32),
        ('d', c_int32),
    ]
    def __lt__(self, other):
        return self.d < other.d
road=[Node() for i in range(1000)]
print(road[0].a)
ch = [Node() for i in range(1000)]
def small(a,b):
    return a.d < b.d
parent=np.empty(1000,dtype=int)

def find(a):  #find root
    if a == parent[a]:
        return a
    else:
        return find(parent[a])

def Union(a,b):
    parent[find(a)] = find(b)
def cost(choseNum, t):
    sum = 0
    for i in range(0, choseNum, 1):
        sum+=ch[i].d
    return sum / t + t * X
def t (choseNum):
    min = cost(choseNum, 1)
    t = 1
    for i in range(2, T, 1):
        if cost(choseNum, i) < min:
            min = cost(choseNum, i)
            t = i
    print(t, "\n")
def kruskal(n, m):
    for i in range(0, n, 1):
        parent[i] = i
    road[0:m] = sorted(road[0:m])
    choseNum = 0
    #跑超過n-1,表圖有cycle，依序找出最小生成樹上的V-1條邊
    j = 0
    for i in range(0, m, 1):
        #i: edge,j: node
        if(j < n-1):
            while find(road[i].a) == find(road[i].b):
                #cycle 不要(已連在一起不要)
                i += 1
            Union(road[i].a, road[i].b)#把a ,b tree串到一起
            ch[choseNum] = road[i]
            choseNum += 1
            j += 1
        else:
            break
    t(choseNum)
    print(choseNum,"\n")
    for i in range(0, choseNum, 1):
        print(ch[i].a, ch[i].b, "\n")

islandNum = int(input("Input islandNum: "))
roadNum = int(input("Input roadNum: "))
T = int(input("魔法設備等級上限: "))
X = int(input("等級一魔法設備之價格: "))
for i in range(0,roadNum,1):
    road[i].a = int(input("Island1 name:　"))
    road[i].b = int(input("Island2 name:　"))
    road[i].d = int(input("Basic cost:　"))
    '''road = []
    road.append(Node(a, b, d))'''
kruskal(islandNum,roadNum)