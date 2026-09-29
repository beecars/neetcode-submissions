class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l_prods = [1] * len(nums)
        r_prods = [1] * len(nums)

        for idx in range(1, len(nums)):
            l_prods[idx] = l_prods[idx - 1] * nums[idx - 1]

        for idx in range(len(nums) - 2, -1, -1):
            r_prods[idx] = r_prods[idx + 1] * nums[idx + 1]

        return [l_prods[idx] * r_prods[idx] for idx in range(len(nums))]