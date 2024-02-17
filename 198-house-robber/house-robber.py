class Solution:
    def rob(self, nums: List[int]) -> int:
        o = e = 0
        for num in nums:
            tempt = max(num + o, e)
            o = e
            e = tempt
        return e