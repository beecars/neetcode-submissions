class Solution:

    def charCounts(self, s: str) -> dict:
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        return char_counts

    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = self.charCounts(s)
        t_counts = self.charCounts(t)
        return s_counts == t_counts
        