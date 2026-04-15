class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_chars = {char: s.count(char) for char in s}
        t_chars = {char: t.count(char) for char in t}

        if s_chars == t_chars:
            return True
        else: 
            return False
