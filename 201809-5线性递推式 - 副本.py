
from collections import deque

m, l, r = map(int, input().split())
k = [0]
for i in map(int, input().split()):
    k.append(i-k[-1])
print(k)

ans = [1,]
q = deque([[0]],maxlen = m)
print(q)
input()
for n in range(1, r+1):
    tm = []
    for i in range(0,min(n,m)):
        tm.append(q[n-1][i]+k[])

for n in range(1,r+1):
    tm = []
    for i in range(1,min(n,m)+1):
        tm.append()
        tm += k[i-1]*ans[n-i]
    ans.append(tm%998244353)
#print(ans)
for i in range(l,r+1):
    print(ans[i])
