class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # index and the value have the same unit

        # for each pair of heights, need area
        max_area = 0

        for lidx in range(len(heights)-1):
            for ridx in range(lidx+1, len(heights)):
                water_width = ridx - lidx
                water_height = min(heights[lidx], heights[ridx])
                max_area = max(max_area, water_height*water_width)

        return max_area


