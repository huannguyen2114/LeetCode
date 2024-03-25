class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        for i in s:
            if i in "({[":
                st.append(i)
            elif st and st[-1] == mp[i]:
                st.pop()
            else:
                st.append(i)
        if len(st) != 0:
            return False
        return True