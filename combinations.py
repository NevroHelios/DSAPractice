def goo(nums, t, lis:list = [], ans:list = [], idx = 0):
    if lis and sum(lis) == t:
        return ans.append(lis)
        
    goo(nums, t, lis = lis.append(nums[idx]), ans =ans, idx=idx)
    goo(nums, t, lis = lis.append(nums[idx]), ans =ans, idx = idx+1)
    
    
nums = [2, 3, 6, 7]
t = 7

print(goo(nums, t)) 