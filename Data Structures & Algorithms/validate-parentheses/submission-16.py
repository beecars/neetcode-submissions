class Solution:
    @staticmethod
    def isMatch(ch_open, ch_close) -> bool:
        """
        """
        is_match = False
        if ch_open == '[' and ch_close == ']' or \
           ch_open == '(' and ch_close == ')' or \
           ch_open == '{' and ch_close == '}':
           is_match = True
        
        return is_match

    def isValid(self, s: str) -> bool:
        """ A closing bracket has to match the last open bracket.
        """
        open_def = ('[', '{', '(')
        opens = []

        for ch in s:

            # If open bracket, add to open stack. 
            if ch in open_def:
                opens.append(ch)

            # If close bracket, check if valid. 
            elif opens and self.isMatch(opens[-1], ch):
                opens.pop()
                continue

            # Otherwise, invalid.
            else: 
                return False

        return True if len(opens) == 0 else False
