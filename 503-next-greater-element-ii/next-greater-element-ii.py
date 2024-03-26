class Solution:
    # This problem is the same as the Next Greater Element except for the circular array.
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
       # In order to solve this problem, we have to change this problem to the Next Greater Element by 
       # 1. Duplicate the linked list
       # 2. for loop with 2n in and use %

        tempt = nums[:]
        for val in nums:
            tempt.append(val)
        st = []
        print(tempt)
        ans = [-1] * len(nums)
        for i in range(len(tempt) - 1, - 1, -1):
            while st and st[-1] <= tempt[i]:
                st.pop()
            if i < len(nums):
                print(i)
                if st:
                    ans[i] = st[-1]
            st.append(tempt[i])
        return ans

