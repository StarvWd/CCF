

n, q = map(int, input().split())

A = [_ for _ in range(n+1)]

U = [314882150829468584, 427197303358170108, 1022292690726729920, 1698479428772363217, 2006101093849356424]

def f(x):
    return (x%2009731336725594113)%2019

for _ in range(q):
    l, r = map(int, input().split())
    s = 0
    for i in range(l, r+1):
        s+=f(A[i])
    print(s)
    t = s%5
    for i in range(l, r+1):
        A[i] *= U[t]
'''
4 4
1 3
3 4
3 3
1 3
'''
