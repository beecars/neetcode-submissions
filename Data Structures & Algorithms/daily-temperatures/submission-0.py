class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        """
        result = [0]*len(temperatures)

        for tidx, t in enumerate(temperatures):
            for ftidx, ft in enumerate(temperatures[tidx:]):
                if t-ft < 0:
                    result[tidx] = ftidx
                    break        
        return result
        