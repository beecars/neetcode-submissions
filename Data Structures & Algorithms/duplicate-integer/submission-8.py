class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        list_size = len(nums)
        set_size = len(set(nums))

        return list_size != set_size