

N,M = map(int,(input().split()))

dic = []
for i in range(N):
    s = list(map(int, input().split()))
    s.append(i + 1)
    dic.append(s)

for _ in range(M):
    x, y = map(int, (input().split()))

    for j in range(N - 1, -1, -1):
        win = dic[j]
        if win[0]<=x<=win[2] and win[1]<=y<=win[3]:
            print(win[4])
            dic.pop(j)
            dic.append(win)
            break;
    else:
        print('IGNORED')