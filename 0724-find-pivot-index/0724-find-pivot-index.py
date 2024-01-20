class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)
        for idx, ele in enumerate(nums):
            r -= ele
            if l == r:
                return idx  
            l += ele
        return -1 