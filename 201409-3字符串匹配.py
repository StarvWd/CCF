


tar = input()
flag = int(input())
n = int(input())
def judge(a, b ,f):
    b = b.upper() if f==0 else b
    if a in b:
        return True
    return False
tar = tar.upper() if flag==0 else tar
for i in range(n):
    qes = input()
    if judge(tar,qes,flag):
        print(qes)
