

m, l, r = map(int, input().split())

k = list(map(int, input().split()))

ans = [1,]

for n in range(1,r+1):
    tm = 0
    for i in range(1,min(n,m)+1):
        tm += k[i-1]*ans[n-i]
    ans.append(tm%998244353)
#print(ans)
for i in range(l,r+1):
    print(ans[i])
