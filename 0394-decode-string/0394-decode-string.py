class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        st = ""
        nu = 0
        for x in s:
            if x == '[':
                stack.append(st)
                stack.append(nu)
                st = ""
                nu = 0
            elif x == ']':
                pre_nu = stack.pop()
                pre_st = stack.pop()
                st = pre_st + pre_nu * st
            elif x.isdigit():
                nu = nu*10 + int(x)
            else:
                st = st + x
        
        return st
            
                