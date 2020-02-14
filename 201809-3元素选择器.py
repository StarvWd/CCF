'''
11 5
html
..head
....title
..body
....H1
....P #subtitle
....div #main
......h2
......p #one
......div
........p #two
p
#subtitle
'''

n, m = map(int, input().split())

html = []
css = []
tab = []
ancestor = {}
for _ in range(n):
    st = input().split('.')
    html.append(st.pop())
    tab.append(len(st)/2)

for i in range(n):
    ancestor[i] = []
    for j in range(i-1,0-1,-1):
        if tab[j] == tab[i]:
            ancestor[i] = ancestor[j]
            break
        elif tab[j] < tab[i]:
            ancestor[i].append(j)
            ancestor[i].extend(ancestor[j])
            break
#print(html)        
#print(ancestor)
def op1(css):
    ans = []
    for i in range(n):
        if css == html[i].split()[0].upper():
            ans.append(i)
    return ans

def op2(css):
    ans = []
    for i in range(n):
        if css == html[i].split()[-1]:
            ans.append(i)
    return ans

def op3(css):

    ans = []
    con = []
    for i in css:
        con.append(op2(i) if i[0] == '#' else op1(i.upper()))
    child = con.pop()
    num = len(con)-1
    for i in child:
        num = len(con)-1
        #print('******',i)
        way = ancestor[i]
        for j in way:
            if j in con[num]:
                num -= 1
            if num < 0:
                ans.append(i)
                break
    return ans

for _ in range(m):
    css = input().split()
    if len(css) != 1:
        ans = op3(css)
    elif css[0][0] == '#':
        ans = op2(css[0])
    else:
        ans = op1(css[0].upper())
    print(len(ans), end = ' ')
    print(' '.join(map(lambda i:str(i+1), ans)))
