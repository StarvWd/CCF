

n = int(input())

ans = [0,0,0,0]
idx = 1
tm = 1
while tm <= n:
    if idx%7==0 or '7' in str(idx):
        ans[idx%4]+=1
    else:
        tm+=1
    idx+=1
for i in range(1,4):
    print(ans[i])
print(ans[0])
