class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_maps = {}
        for word in strs:
            sword = ''.join(sorted(word))
            char_maps[sword] = char_maps.get(sword, []) + [word]
        return [key for key in char_maps.values()]