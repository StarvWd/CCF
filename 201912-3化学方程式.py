
'''
11
H2+O2=H2O
2H2+O2=2H2O
H2+Cl2=2NaCl
H2+Cl2=2HCl
CH4+2O2=CO2+2H2O
CaCl2+2AgNO3=Ca(NO3)2+2AgCl
3Ba(OH)2+2H3PO4=6H2O+Ba3(PO4)2
3Ba(OH)2+2H3PO4=Ba3(PO4)2+6H2O
4Zn+10HNO3=4Zn(NO3)2+NH4NO3+3H2O
4Au+8NaCN+2H2O+O2=4Na(Au(CN)2)+4NaOH
Cu+As=Cs+Au
'''
n = int(input())

def findDigit(i): # 提取数字，并返回提取完的位置下标
    num=''
    while i < len(el) and el[i].isdigit():
        num += el[i]
        i+=1
    num = int(num) if num else 1 # 若没有则默认1
    return num, i

def findLetter(i): # 提取一个元素符号，Ag，O，并返回提取完的位置下标
    if el[i].isupper():
        let = el[i]
    else:
        return '', i
    i += 1
    while i < len(el) and el[i].islower():
        let += el[i]
        i+=1
    return let, i
        
def judge(i):   # 获取当前i下标块的结果， 由 tmp 储存返回
    tmp = {}
    if el[i] == '(':    # 处理 括号+后缀(NO3)2 部分， 由于存在嵌套，使用递归， 并存入tmp
        i+=1
        while el[i]!=')':       # 循环查找，直到达到临界条件。临界条件：碰到 右括号 即退出。 
            i, tmp_c = judge(i)
            for k in tmp_c:
                tmp[k] = tmp.get(k, 0) + tmp_c[k]            
        i += 1
        num, i = findDigit(i)   # 退出递归后，获取括号后缀，并乘以tmp中的结果
        for k in tmp:
            tmp[k] *= int(num)
    else:               # 处理 元素+后缀O2 部分， 较简单， 分别提取元素与数字， 并存入tmp
        s, i = findLetter(i)
        num, i = findDigit(i)
        tmp[s] = tmp.get(s,0) + int(num)
    return i, tmp


def analyze(el): # 分析结果由ans_t返回
    el = list(el)
    ans_t = {}
    
    i = 0 # 记录下标位置
    el_num, i = findDigit(i) # 获取前缀系数，乘以ans_t结果
    
    while True: # 循环分块查找，每一个 括号+后缀(NO3)2 或 元素+后缀O2 为一部分
        
        i, tm = judge(i) # tm为查找结果
        for k in tm:     # 将tm汇总到ans_t中
            ans_t[k] = ans_t.get(k,0)+tm[k]
        #print(tm)    
        if i >= len(el): # 下标越界，则查找结束
            break
    
    if el_num != 1:     # 结果乘以前缀系数
        for k in ans_t:
            ans_t[k] *= el_num
    return ans_t        # 返回表达式查询结果


for _ in range(n):
    left, right = input().split('=') # 分为左右两部分
    
    left = left.split('+')          # 提取各个表达式
    right = right.split('+')
    left_ans = {}                   # 保存最终统计结果
    right_ans = {}
    #print(left,right)
    
    for el in left:                 # 分析每个表达式的成分
        ans_t = analyze(el)
        for k in ans_t:     # 汇总到left_ans
            left_ans[k] = left_ans.get(k,0)+ans_t[k] 
    #print(left_ans)
    for el in right:
        ans_t = analyze(el)
        for k in ans_t:     # 汇总到right_ans
            right_ans[k] = right_ans.get(k,0)+ans_t[k] 
    #print(right_ans)
     
    if right_ans == left_ans:
        print('Y')
    else:
        print('N')
