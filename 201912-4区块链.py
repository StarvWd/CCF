
'''
BFS
每次k个操作之前，无论查询或生成，都需要将 广搜 推进到该时刻 b，

node 保存节点主链
que 队列维持广搜进度，保存节点编号，时间，传播的主链
因为node与que均以list保存主链
故：node与que相互赋值更改主链时，使用copy或[:]深拷贝，防止更改
'''


from collections import deque
#from copy import copy

def query(b):
    '''
    无论查询还是生成，均将b时刻之前的所有广搜队列的访问执行
    '''
    global node, que
    while len(que) and que[0][1] <= b: # 推进所有小于b的搜索
        ind, ti, chain = que.popleft()
        if len(node[ind]) < len(chain) or (len(node[ind])==len(chain) and node[ind][-1] > chain[-1]):
            # 满足条件则更新主链，并向下传播搜索，否则停止
            node[ind] = chain[:] # copy(chain)
            for i in graph[ind]:
                que.append([i, ti+t, chain])

n, m = map(int, input().split())
graph = {}                          # 邻接表
node = [[0] for _ in range(n+1)]    # 节点保存的主链
que = deque()                       # 广搜维持的队列，每项包括 节点编号，时间，主链
# 初始化邻接表
for i in range(1,n+1):
    graph[i] = []
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
t, k = map(int, input().split())

for _ in range(k):
    a = list(map(int, input().split()))
    if len(a) == 2: # 查询 a节点 b时刻 的主链
        a,b = a  
        query(b) # 执行 b时刻 之前 所有传播
        ans = node[a] # 获取b时刻a的主链
        
        print(len(ans), end=' ')
        for i in ans:
            print(i, end=' ')
        print()
        
    elif len(a) == 3:
        a,b,c = a # a节点 b时刻 主链增加 c
        query(b)  # 执行 b时刻之前所有传播
        
        node[a].append(c)  # 添加主链，并在a上执行广搜，进队
        for i in graph[a]:
            que.append([i, b+t, node[a][:]]) # copy(node[a])

'''
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
1 27
1 1 1
2 1 2
3 1 3
4 1 4
5 1 5
1 1
2 1
3 1
4 1
5 1
1 2
2 2
3 2
4 2
5 2
1 10 10
2 11 9
1 11
2 11
3 11
4 11
5 11
1 12
2 12
3 12
4 12
5 12
'''
'''
15 13
1 2
2 3
3 4
4 5
1 6
6 7
7 8
8 9
1 10
10 11
11 12
12 13
14 15
6 28
1 1 1
1 2 2
1 6
2 7
13 7
9 7
5 7
3 14
8 14
5 14
11 14
9 25
5 25
13 25
9 29 3
5 29 4
13 29 5
1 53
2 59 6
2 59
1 1000
3 1000
8 1000
9 1000
10 1000
13 1000
14 1000
15 1000
'''
