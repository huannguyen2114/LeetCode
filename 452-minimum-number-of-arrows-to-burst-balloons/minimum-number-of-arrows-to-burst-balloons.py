class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort the points based on the first value
        points.sort(key = lambda point: point[1])
        print(points)
        # define a result and k for compare purpose
        res = 1
        k = points[0][1]

        for x in points[1:]:
            if x[0] > k:
                res += 1
                k = x[1]
            else:
                k = min(k, x[1])
        
        return res