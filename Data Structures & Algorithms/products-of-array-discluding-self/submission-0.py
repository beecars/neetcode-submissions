class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lefts = [1 for _ in range(len(nums))]
        rights = [1 for _ in range(len(nums))]
        for i in range(len(nums)-1):
            lefts[i+1] = nums[i] * lefts[i]
            rights[len(nums)-2-i] = nums[len(nums)-1-i] * rights[len(nums)-1-i]

        pes = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            pes[i] = lefts[i] * rights[i]
            
        return pes