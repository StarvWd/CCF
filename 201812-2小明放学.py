
'''
按照习惯，重新规定：
红 - 1
绿 - 2
黄 - 3
'''
lig = list(map(int, input().split()))
lig[1],lig[2] = lig[2],lig[1]
n = int(input())
ans = 0
def find(of,ti):      
    while ti >= lig[of]:
        ti = ti - lig[of]
        of = (of+1)%3
    return of+1, lig[of]-ti
    
for _ in range(n):
    of, ti = map(int, input().split())
    if of == 2:
        of = 3
    elif of == 3:
        of = 2
        
    if of == 0:
        ans += ti
        #print(of,ti)
    else:
        of, ti = find(of-1, lig[of-1]-ti+ans%sum(lig))
        #print(of,ti)
        if of == 1:
            ans += ti
        elif of == 3:
            ans += ti+lig[0]
    #print(ans)   
print(ans)
