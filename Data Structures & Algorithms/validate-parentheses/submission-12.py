class Solution:

    def isValid(self, s: str) -> bool:
        """   
        """
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        bracket_stack = []

        # Iterate through brackets. 
        for bracket in s:

            # Check for open bracket. 
            if bracket in bracket_map:
                bracket_stack.append(bracket_map[bracket])
        
            else:
                if not bracket_stack or bracket != bracket_stack[-1]:
                    return False
                bracket_stack.pop()

        if len(bracket_stack) == 0:
            return True
        else:
            return False
                




