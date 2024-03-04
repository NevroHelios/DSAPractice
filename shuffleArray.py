# Amaazon (Medium)
#GfG
def shuffleArray( arr:list, n):
        # Your code goes here
        for i in range(int(n/2)):
            arr.insert(2 *i + 1, arr[i + int(n/2)])
            del arr[i + int(n/2) + 1]
        return arr

arr = [5, 9, 7, 7, 9, 6, 8, 9, 10, 1]

print(shuffleArray(arr, len(arr)))  #[5, 6, 9, 8, 7, 9, 7, 10, 9, 1]




class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:        
        nums1, nums2 = nums[0], nums[1]
        ans, s0, s1 = 1,1,1

        for a1,b1,a2,b2 in zip(nums1, nums1[1:], 
                        nums2, nums2[1:]):

            s0, s1 = (max(s0*(a1 <= b1),  s1*(a2 <= b1))+1, max(s0*(a1 <= b2),  s1*(a2 <= b2))+1)

        ans = max(ans, s0, s1)

        return ans