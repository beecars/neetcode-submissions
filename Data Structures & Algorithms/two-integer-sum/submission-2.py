class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_from_sum = {} # num: idx

        for nidx, num in enumerate(nums):
            
            diff = target - num
            
            if diff in diff_from_sum:
                return [diff_from_sum[diff], nidx]

            else:
                diff_needed = num
                diff_from_sum[num] = nidx

            print(diff_from_sum)
