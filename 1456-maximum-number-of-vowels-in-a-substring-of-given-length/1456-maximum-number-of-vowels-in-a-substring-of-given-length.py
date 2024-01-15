class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        curr_vowels = 0
        
        # Count vowels in the first window of length k
        for i in range(k):
            if s[i] in vowels:
                curr_vowels += 1
        
        max_vowels = curr_vowels
        
        # Slide the window and update the count of vowels
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                curr_vowels -= 1
            if s[i] in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
        
        return max_vowels