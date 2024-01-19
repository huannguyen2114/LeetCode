class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = []
        a.append(0)
        for i in range(0, len(gain)):
            a.append(a[i] + gain[i])
        
        return max(a)