
'''
5
4 10 0 9 0
4 10 -2 7 0
2 10 0
4 10 -3 5 0
4 10 -1 8 0
'''
'''
4
4 74 -7 -12 -5
5 73 -8 -6 59 -4
5 76 -5 -10 60 -2
5 80 -6 -15 59 0
'''
'''****************************
*****************理解题意********************
**************************************'''
n = int(input())

t, d, e = 0, 0, 0
# t：剩余果子总数
# d：掉果子总数
# e：连续掉果子总数
con = []    #保存数据
now = []    #记录当前果子
flg = [0]*n #记录是否掉果子
for i in range(n):
    n1, n2,*a = map(int, input().split())
    now.append(n2)
    con.append(a)


for i in range(n):
    for j in con[i]:       
        if j <= 0:
            now[i] += j
        elif j > 0 and j != now[i]:
            flg[i] = 1
            now[i] = j
        
for i in range(n):
    l = i-1
    r = i+1
    if l == -1:
        l = n-1
    if r == n:
        r = 0
    if flg[i] and flg[l] and flg[r]:
        e += 1
        
d = sum(flg)
t = sum(now)
print(t,d,e)
