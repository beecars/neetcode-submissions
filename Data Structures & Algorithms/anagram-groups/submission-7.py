class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        
        for s in strs:
            freqs = [0] * 26
            s = s.lower()
            for char in s:
                cidx = ord(char) - ord('a')
                freqs[cidx] = freqs[cidx] + 1
            skey = tuple(freqs)
        
            if skey in groups:
                groups[skey].append(s)
            else:
                groups[skey] = [s]

        return [v for v in groups.values()]