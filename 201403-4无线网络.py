'''
最短路径使用，广度优先搜索bfs
'''

n, m, k, r = map(int,input().split())
r = r*r
dic = {}
loc = [list(map(int,input().split())) for i in range(n+m)]
'''for i in range(n+m):
    s = list(map(int,input().split()))
    loc.append(s)
print(loc)'''
def distince(a, b):
    if (a[0]-b[0])**2 + (a[1]-b[1])**2 <= r:
        return True
    return False
for i in range(n+m):
    dic[i] = []
for i in range(n+m):
    for j in range(i+1,n+m):
        if distince(loc[i],loc[j]):
            dic[i].append(j)
            dic[j].append(i)
#print(dic)

flag = [False] * (n + m)
def bfs(index):
    node = [index]
    res = [0] * (n + m)
    step = [0] * (n + m)
    head = 0
    while head != len(node):
        index = node[head]
        head += 1
        if index == 1:
            return step[1]-1
        flag[index] = True
        for i in dic[index]:
            if flag[i] == False:
                if i >= n and res[i]+1 <= k or i < n:
                    node.append(i)
                    flag[i] = step
                    res[i] = res[index]+1
                    step[i] = step[index]+1

ans = bfs(0)
print(ans)
'''
flag = [False] * (n + m)
def dfs(index, now_k, now_node):  
    深度优先搜索
    :param index: 当前节点
    :param now_k: 约束条件K
    :param now_node: 走过节点数，路径长度
    :return:
    global node
    if flag[index] or now_k > k:
        return
    flag[index] = True
    node+=1
    if index == 1 and now_node < node:
        node = now_node
        return
    if index >= m:
        now_k+=1
    for i in dic[index]:
        dfs(i,now_k, now_node)

dfs(0, 0, 0)'''
