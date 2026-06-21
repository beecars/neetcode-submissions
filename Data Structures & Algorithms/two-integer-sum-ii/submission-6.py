class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers is in increasing order
        # start in middle
        # "big" index and "small" index. 
        # big starts in middle.

        for sidx in range(len(numbers)):
            for bidx in range(len(numbers[sidx:])):
                twosum = numbers[bidx + sidx] + numbers[sidx]
                if twosum == target:
                    return [sidx + 1, bidx + sidx + 1]
                elif twosum > target:
                    break