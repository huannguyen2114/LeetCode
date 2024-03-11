class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        frequency = Counter(s)
        for i in range(len(order)):
            if order[i] in s and frequency[order[i]] == 1:
                res += order[i]
            elif order[i] in s and frequency[order[i]] > 1:
                while frequency[order[i]] > 0:
                    res += order[i]
                    frequency[order[i]] -= 1
        tempt = ""
        for i in range(len(s)):
            if s[i] in res:
                continue
            tempt += s[i]
        
        return res + tempt