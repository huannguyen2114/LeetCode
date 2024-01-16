class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        res = ""
        l = len(a) - 1
        while l >= 0:
            res = res + a[l] + " "
            l -= 1
        
        res = res.strip()
        return res