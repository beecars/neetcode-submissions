class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        """
        record = []
        for op in operations:
            try:
                record.append(int(op))
            except:
                pass
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
        
        return sum(record)

