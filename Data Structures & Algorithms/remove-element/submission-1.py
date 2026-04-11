class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """ Remove all val elements form nums in-place. Order of non-val elements does not matter.
            Do not need to consider elements beyond the first k positions. The first k elemets of
            nums must contain only elements not equal to val. Return k. 
        """
        n = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[n] = nums[j]
                n += 1

        return n

                
