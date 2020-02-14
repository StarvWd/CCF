

'''
7
1 2
2 1
0 0
1 1
1 0
2 0
0 1

2
0 0
-100000 10

11
9 10
10 10
11 10
12 10
13 10
11 9
11 8
12 9
10 9
10 11
12 11
'''
n = int(input())

rub = {}

for _ in range(n):
    x,y = map(int, input().split())
    rub[(x,y)] = -1

#print(rub)
for key in rub:
    x,y = key
    if rub.get((x-1,y), 0) and rub.get((x+1,y), 0) and rub.get((x,y+1), 0) and rub.get((x,y-1), 0):
        rub[key] += 1

        if rub.get((x-1,y-1), 0):
            rub[key] += 1
        if rub.get((x-1,y+1), 0):
            rub[key] += 1
        if rub.get((x+1,y-1), 0):
            rub[key] += 1
        if rub.get((x+1,y+1), 0):
            rub[key] += 1
#print(rub)
ans = [0]*6
for key in rub:
    ans[rub[key]] += 1
#print(ans)
for i in range(5):
    print(ans[i])
