# def combinationSum2(candidates, target: int):
def check(nums, t, lis=[], idx=0):

    if t == 0:
        ans.append(lis[:])
        return

    for i in range(idx, len(nums)):
        
        if i > idx and nums[i] == nums[i-1]:
            continue      
        if t < nums[i]:
            break
        
        lis.append(nums[i])
        check(nums, t-nums[i], lis, i+1)
        lis.pop()    
        

# Test case 1:
candidates = [1,1,1,2,2]
target = 4

# print(combinationSum2([1, 1, 1, 2, 2], 4))
ans = []
check(nums=sorted(candidates), t=target)
print(ans)