from copy import deepcopy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for ridx in range(9):
            for cidx in range(9):
                num = board[ridx][cidx] 
                if num == ".":
                    continue
                num = int(num)

                bidx = (ridx // 3) * 3 + cidx // 3 

                if num in rows[ridx] or num in cols[cidx] or num in boxes[bidx]:
                    return False

                rows[ridx].add(num)
                cols[cidx].add(num)
                boxes[bidx].add(num)

        return True

