class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sum_to_target = {}   # Map of val: idx

        for idx, num in enumerate(nums):
            if num in sum_to_target:
                return [sum_to_target[num], idx]
            need = target - num
            sum_to_target[need] = idx