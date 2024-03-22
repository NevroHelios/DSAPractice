def goo(nums, t, lis = [], idx=0):
    if idx == len(nums):
        if t == 0:
            ans.append(lis[:])
        return
    if t >= nums[idx]:
        lis.append(nums[idx])
        goo(nums, t-nums[idx], lis, idx)
        lis.pop()
    goo(nums, t, lis, idx+1)

ans = []

candidates = [2, 3, 6, 7]
target = 7

goo(nums=candidates, t=target)

print(ans) 

# print(goo(nums, t)) 