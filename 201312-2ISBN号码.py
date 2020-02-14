isbn = input()

num = ''.join(isbn.split('-'))

ans = 0
for i in range(9):
    ans += int(num[i])*(i+1)
ans = 'X' if str(ans%11)=='10' else str(ans%11)

if ans == num[-1]:
    print('Right')
else:
    print(isbn[:-1]+str(ans))