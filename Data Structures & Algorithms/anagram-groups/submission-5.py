class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:

            # Create frequency map. 
            s_freq_map = {}
            for ch in s:
                ch_count = s_freq_map.get(ch, 0)
                s_freq_map[ch] = ch_count + 1

            s_freq_map_hashable = tuple(sorted(s_freq_map.items()))

            # Check for equivalence. 
            if s_freq_map_hashable in anagrams:
                anagrams[s_freq_map_hashable].append(s)
            else:
                anagrams[s_freq_map_hashable] = [s]

        return list(anagrams.values())