n, m = map(int, input().split())

ans = 0
if (n*m)%6 != 0:
    print(0)
elif m == 2: 
    ans = int(2**(n/3))
    print(ans)
elif n <= 6 and m <=6:
    dic = [[0,0,0,0,0,0],
           [0,0,2,0,0,4],
           [0,2,0,4,0,8],
           [0,0,4,0,0,18],
           [0,0,0,0,0,64],
           [0,4,8,18,64,160]
        ]
    ans = dic[n-1][m-1]
    print(ans)
else:
    dic = [[0]*(7) for i in range(n+1)]
    dic[3][2] = dic[2][3] = 2
    dic[2][6] = dic[3][4] = 4
    dic[3][6] = 8
    #print(dic)
    for i in range(4, n+1):
        for j in range(1, 7): 
            tm1,tm2 = 0, 0              
            for k in range(1,i):
                tm1 += (dic[k][j]*dic[i-k][j])
            
            for k in range(1,j):
                tm2 += (dic[i][k]*dic[i][j-k])
            print(i, j, int(i/2), tm1+tm2)        
            dic[i][j] = tm1+tm2
    print(dic)
