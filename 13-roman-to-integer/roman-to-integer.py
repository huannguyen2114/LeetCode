class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a result variable and a "roman to integer" map
        res = 0
        
        rti = {
            "I" : 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        # Looping through each word
        for i in range(len(s) - 1):
            # If the smaller value come before the larger one, the minus the result
            if rti[s[i]] < rti[s[i+1]]:
                res -= rti[s[i]]
            # Else add the value with the right number in the map

            else:
                res += rti[s[i]]
        
        res += rti[s[len(s) - 1]]
        return res