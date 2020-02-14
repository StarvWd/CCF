
n = int(input())

s = list(map(int, input().split()))

num = [0] * 1000

for i in s:
    num[i]+=1
    print(num[i], end=' ')
