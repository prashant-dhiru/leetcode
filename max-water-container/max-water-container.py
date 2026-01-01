class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1 7 2 5 4 7 3 6
        # l=0 r=1, m=0, a=1*1

        l, r = 0, len(heights)-1
        max_area = 0
        while l < r :
            a = (r-l) * min(heights[l], heights[r])
            max_area = max(max_area, a)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_area