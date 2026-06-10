class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        """
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        
        is_palindrome = True
        for lidx in range(len(s)):
            ridx = len(s) - lidx - 1

            if s[lidx] != s[ridx]:
                is_palindrome = False
                break
            elif lidx >= ridx:
                break

        return is_palindrome