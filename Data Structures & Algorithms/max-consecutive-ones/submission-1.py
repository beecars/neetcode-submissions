class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """ Iterate through, count consecutive, store max. O(n).
        """
        max_consec = 0
        cur_consec = 0
        for num in nums:
            if num == 1:
                cur_consec += 1
                max_consec = max(cur_consec, max_consec)
            else:
                cur_consec = 0
        
        return max_consec
            
