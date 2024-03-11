class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a result variable
        res = ""

        # Define a map storing integer to roman value

        itr = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        # convert the num to string for easier looping
        s = str(num)

        for i in range(len(s)):
            n = len(s) - (i + 1)
            if s[i] == "4":
                val_five = itr[5 * 10 ** n]
                val_minus_one = itr[1 * 10 ** n]
                res = res + val_minus_one + val_five
            elif s[i] == "9":
                val_one = itr[1 * 10 ** (n + 1)]
                val_minus_one = itr[1 * 10 ** n]
                res = res + val_minus_one + val_one
            else:
                if int(s[i]) >= 5:
                    val_five = itr[5 * 10 ** n]
                    res += val_five
                    tempt = int(s[i]) - 5
                    while tempt > 0:
                        val_one = itr[1 * 10 **n]
                        res += val_one
                        tempt -= 1
                else:
                    tempt = int(s[i])
                    while tempt > 0:
                        val_one = itr[1 * 10 **n]
                        res += val_one
                        tempt -= 1
        
        return res
