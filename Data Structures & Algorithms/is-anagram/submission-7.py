class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_counts = {}
        t_counts = {}

        if len(s) != len(t):
            return False

        for s_char, t_char in zip(s, t):
            
            s_counts[s_char] = s_counts.get(s_char, 0) + 1
            t_counts[t_char] = t_counts.get(t_char, 0) + 1

        print(s_counts)
        print(t_counts)

        return s_counts == t_counts
