def judge(x, y, s):
    # 下标合法，当前未访问过的下标，返回true
    if x < 0 or x >= c or y < 0 or y >= l or s[x][y] == True:
        return False
    return True


def dfs(x, y):
    if judge(x, y, sign_st) == False or m[x][y] == '#' or sign_st[x][y]:
        return
    sign_st[x][y] = True
    if m[x][y] == '|':
        dfs(x - 1, y)
        dfs(x + 1, y)
    elif m[x][y] == '-':
        dfs(x, y - 1)
        dfs(x, y + 1)
    elif m[x][y] == '.':
        dfs(x + 1, y)
    elif m[x][y] in '+ST':
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)


# 反向搜索
def dfs_re(x, y):
    sign_ed[x][y] = True
    if judge(x - 1, y, sign_ed) and m[x - 1][y] in '+|.':
        dfs_re(x - 1, y)
    if judge(x + 1, y, sign_ed) and m[x + 1][y] in '+|TS':
        dfs_re(x + 1, y)
    if judge(x, y - 1, sign_ed) and m[x][y - 1] in '+-TS':
        dfs_re(x, y - 1)
    if judge(x, y + 1, sign_ed) and m[x][y + 1] in '+-TS':
        dfs_re(x, y + 1)


# m = [['--+-+'],
#      ['..|#.'],
#     ['..|##'],
#    ['S-+-T'],
#   ['####.']]

c, l = input().split()
c = int(c)
l = int(l)
m = []
for i in range(c):
    m.append(list(input()))
# print(m)
start = []
end = []
for i in range(c):
    for j in range(l):
        if m[i][j] == 'S':
            start.extend([i, j])
        elif m[i][j] == 'T':
            end.extend([i, j])

sign_st = [[False] * l for i in range(c)]
sign_ed = [[False] * l for i in range(c)]
dfs(start[0], start[1])

if sign_st[end[0]][end[1]] != True:
    print("I'm stuck!")
else:
    dfs_re(end[0], end[1])
    # print(sign_st)
    # print(sign_ed)
    ans = 0
    for i in range(c):
        for j in range(l):
            if sign_st[i][j] == True and sign_ed[i][j] == False:
                ans += 1;
    print(ans)
