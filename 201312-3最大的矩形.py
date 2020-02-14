
'''
暴力循环
'''
n = int(input())
s = list(map(int,input().split()))

best = 0
for i in range(n):
    height = s[i]
    for j in range(i,n):
        '''这里使用前一个的高度，避免计算最小值带来的时间损耗'''
        if s[j] < height:
            height = s[j]
        tmb = height*(j-i+1)
        if best < tmb:
            best = tmb
print(best)