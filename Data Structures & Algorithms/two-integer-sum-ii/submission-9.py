class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lidx = 0
        hidx = len(numbers) - 1

        while True:
            sum = numbers[lidx] + numbers[hidx]
            if sum == target:
                return([lidx+1, hidx+1])
            elif sum < target:
                lidx+=1
            else:
                hidx-=1