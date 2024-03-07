class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # Since the nums range is from 1 to 100, so we can use Checked Array (Mang danh dau)
        checked = [0] * 101

        for num in nums:
            checked[num] += 1
        res = 0
        for num in nums:
            if checked[num] == 1:
                res += num
        
        return res