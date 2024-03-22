class Solution:
    def permute(self, nums):
        res = []

        if len(nums) == 1:
            return [nums.copy()]

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            # print(perms)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
