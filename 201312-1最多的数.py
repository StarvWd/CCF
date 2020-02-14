
n = int(input())

s = map(int,input().split())

nums = [0]*10002

for i in s:
    nums[i]+=1
print(nums.index(max(nums)))