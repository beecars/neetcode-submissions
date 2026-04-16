class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_inds = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if num_inds.get(diff, None) is not None:
                return [num_inds[diff], idx]
            num_inds[num] = idx