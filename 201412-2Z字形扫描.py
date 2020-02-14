n = int(input())

dic = []

for i in range(n):
    dic.append(list(map(int, input().split())))

#print(dic)

if n == 1:
    print(dic[0][0])
else:
    x, y = 0, 0

    ind = (n-1)//2
    print(dic[x][y], end=' ')
    for i in range(ind):
        y+=1
        print(dic[x][y], end=' ')
        while y>0:
            x+=1
            y-=1
            print(dic[x][y], end=' ')
        x+=1
        print(dic[x][y], end=' ')
        while x>0:
            x-=1
            y+=1
            print(dic[x][y], end=' ')

        
    if n%2 == 0:
        y+=1
    elif n%2 == 1:
        x+=1
    print(dic[x][y], end=' ')

    for i in range(ind+1):
        while x < n-1:
            x+=1
            y-=1
            print(dic[x][y], end=' ')
        y+=1
        if y == n-1 and x == n-1:
            print(dic[x][y], end=' ')
            break
        print(dic[x][y], end=' ')
        while y < n-1:
            x-=1
            y+=1
            print(dic[x][y], end=' ')
        x+=1
        print(dic[x][y], end=' ')

        

