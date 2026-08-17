class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_groups = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in sorted_groups:
                sorted_groups[s_sorted].append(s)
            else:
                sorted_groups[s_sorted] = [s]
        
        return [value for value in sorted_groups.values()]