class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_maps = {}
        for word in strs:
            sword = ''.join(sorted(word))
            if sword not in char_maps:
                char_maps[sword] = []
            char_maps[sword].append(word)
        return list(char_maps.values())