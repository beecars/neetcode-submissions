class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        char_set = set(s)

        for char in char_set:
            l = 0
            count = 0

            for r in range(len(s)):
                if s[r] == char:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1

                max_len = max(max_len, r - l + 1)

        return max_len