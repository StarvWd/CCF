import math

n = int(input())
flag = [0]*1010
ans = 0
s = list(map(int,input().split()))

for i in s:
    flag[abs(i)]+=1
    if flag[abs(i)] == 2:
        ans+=1
print(ans)