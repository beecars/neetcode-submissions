class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        """
        result = [0] * len(temperatures)
        stack = []
        for tidx, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                resolved = stack.pop()
                result[resolved] = tidx - resolved
            stack.append(tidx)
            
        return result
        