class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        lidx = 0
        ridx = len(heights) - 1
        while lidx < ridx:
            cur_lh = heights[lidx]
            cur_rh = heights[ridx]
            max_area = max(max_area, min(cur_lh, cur_rh) * (ridx - lidx))
            if cur_lh < cur_rh:
                lidx += 1
            else:
                ridx -= 1
        return max_area


