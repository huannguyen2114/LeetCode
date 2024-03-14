class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # check if heights is valid
        if len(heights) == 0 :
            return [0]
        
        # Define ans array
        ans = [0] * len(heights)
        stack = deque()

        # Loop in reverse
        for i in range(len(heights) - 1, -1, -1):
            # Pop the element from the stack until find the number > heights[i]
            while stack and stack[-1] < heights[i]:
                ans[i] += 1
                stack.pop()
            if stack:
                ans[i] += 1
            stack.append(heights[i])
        return ans