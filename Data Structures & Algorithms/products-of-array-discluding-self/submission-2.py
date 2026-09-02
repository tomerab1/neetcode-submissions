class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = 1
        after = 1
        n = len(nums)
        res = [1] * len(nums)

        for i in range(n):
            res[i] *= before
            before *= nums[i]
        
        for i in range(n-1, -1, -1):
            res[i] *= after
            after *= nums[i]
        
        return res