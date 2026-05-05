class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        """
        comp_vals = []
        # Iterate through input.
        for tok in tokens:
            if tok in "+-*/":
                n2 = int(comp_vals.pop()) # The "second"/"right" number
                n1 = int(comp_vals.pop()) # The "first"/"left" number
                if tok == "+":
                    comp_vals.append(n1+n2)
                if tok =="-":
                    comp_vals.append(n1-n2)
                if tok == "*":
                    comp_vals.append(n1*n2)
                if tok == "/":
                    comp_vals.append(int(n1/n2))
            else:
                comp_vals.append(int(tok))

        return comp_vals[0]
