class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """ Replace every element with greatest to the right.
        """
        for i in reversed(range(len(arr))):
            if i == (len(arr)-1):
                highest = arr[i]
                arr[i] = -1
            else:
                tmp = arr[i]
                arr[i] = highest
                highest = max(tmp, highest)
        
        return arr
