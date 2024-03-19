class Solution:
    def reorganizeString(self, s: str) -> str:
        # IDEA: create a hash map to store the frequency of each characters. Then, create a maxHeap to store the character in the incrementing sequence of frequency. For each time, add the character which has the highest frequency except the previous character which was pushed.
        frequency = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in frequency.items()]
        heapq.heapify(maxHeap) #O(n)

        res = ""
        prev = None
        
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        
        return res
