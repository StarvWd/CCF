

tool = input()
a = []
b = []
# 选项分为两组
for i,v in enumerate(tool):
    if v == ':':
        a.append(tool[i-1])
        b.pop()
    else:
        b.append(v)

n = int(input())
for index in range(n):
    s = input().split()
    i,ans = 1,{}
    # 从下标 1 开始，答案存在一个字典中
    while i < len(s) and s[i][0] == '-':
        # 带参数的选项，并判断是否越界
        if s[i][1] in a and i+1<len(s):
            ans[s[i]] = [s[i],s[i+1]]
            i+=1
        # 不带参数选项，直接加入字典
        elif s[i][1] in b:
            ans[s[i]] = [s[i]]
        else:
            break
        i+=1
    valu = []
    for i in sorted(ans):
        valu.append(' '.join(ans[i]))
    print('Case {}:'.format(index+1),' '.join(valu))