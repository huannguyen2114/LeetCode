class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        return sum([k for k in frequency if frequency[k] > len(nums)/2])