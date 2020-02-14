n = int(input())

s = list(map(int, input().split()))


s = sorted(s)

s.append(3.987)
ans = 0
for i in range(len(s)):
    if(abs(s[i]-s[i-1])==1 ):
        ans+=1
print(ans)
