class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        nums_product = 1

        for num in nums:
            nums_product = nums_product * num

        partial_products = [0 for _ in range(len(nums))]
        for idx, num in enumerate(nums):
            if nums[idx] == 0:
                this_partial_product = 1
                for tidx, num in enumerate(nums):
                    if tidx == idx:
                        pass
                    else:
                        this_partial_product = this_partial_product * num
                partial_products[idx] = this_partial_product

            else:
                partial_products[idx] = int(nums_product / nums[idx])

        return partial_products
