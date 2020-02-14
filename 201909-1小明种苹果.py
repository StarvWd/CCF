
n, m = map(int, input().split())

s = []
s1 = []
for i in range(n):
    a0, *a = list(map(int, input().split()))
    s.append(a0)
    a = map(abs, a)
    s1.append(sum(a))
    t = sum(s)-sum(s1)
    k = s1.index(max(s1))
    p = s1[k]
print(t, k+1 ,p )
