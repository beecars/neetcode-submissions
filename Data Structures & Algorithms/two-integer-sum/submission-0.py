class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_inds = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff_inds.get(num, None) is not None:
                return [diff_inds[num], idx]
            diff_inds[diff] = idx