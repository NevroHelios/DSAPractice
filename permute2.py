class Solution:
    def permuteUnique(self, nums):
        res = []

        if len(nums) == 1:
            return [nums.copy()]
        
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permuteUnique(nums)
            for perm in perms:
                perm.append(n)
                if perm not in res:
                    res.append(perm)
            # print('prems', perms)
            # print('resB', res)
            # res.extend(perms)
            # print('resA', res)
            nums.append(n)
        return res