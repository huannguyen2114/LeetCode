class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = []
        for i in range(len(nums)):
            res.append(pre)
            pre *= nums[i]
        
        post = 1
        for i in reversed(range(len(nums))):
            res[i] *= post
            post *= nums[i]
        
        return res

