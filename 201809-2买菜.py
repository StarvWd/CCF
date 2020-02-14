
n = int(input())

tim = [0]*1000000
for _ in range(2*n):
    m,n = map(int, input().split())

    for i in range(m, n):
        tim[i] += 1
ans = 0
for i in tim:
    if i == 2:
        ans+=1
print(ans)
