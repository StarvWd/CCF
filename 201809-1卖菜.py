
n = int(input())

fir = list(map(int, input().split()))


sec = []

for i in range(n):
    tm = [fir[i]]
    if i-1 >= 0:
        tm.append(fir[i-1])
    if i+1 < n:
        tm.append(fir[i+1])
    sec.append((sum(tm)//len(tm)))
print(' '.join(map(str,sec)))
