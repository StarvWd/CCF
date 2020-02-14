n = int(input())


dic = [[0]*100 for i in range(100)]
for i in range(n):
    s = list(map(int, input().split()))
    for j in range(s[0],s[2]):
        for k in range(s[1],s[3]):
            if dic[j][k] == 0:
                dic[j][k]=1
ans = 0
for j in range(100):
    for k in range(100):  
        ans += dic[j][k]

print(ans)
    
