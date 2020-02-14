
'''
红 - 1
绿 - 3
黄 - 2
'''
lig = list(map(int, input().split()))

n = int(input())
ans = 0

for _ in range(n):
    of, ti = map(int, input().split())

    
    if of in [0,1]:
         ans += ti
    elif of == 2:
        ans += ti+lig[0]
    #print(ans)   
print(ans)
