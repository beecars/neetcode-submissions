from copy import deepcopy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        """
        component = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }

        board_parts = {
            "rows": deepcopy(component),
            "cols": deepcopy(component),
            "boxs": deepcopy(component)
        }

        for ridx, row in enumerate(board):

            for cidx, num in enumerate(row):

                if num == '.':
                    continue
                
                num = int(num)
                board_parts["rows"][ridx].append(num)
                board_parts["cols"][cidx].append(num)
                
                if (0 <= ridx < 3) and (0 <= cidx < 3):
                    board_parts["boxs"][0].append(num)
                elif (0 <= ridx < 3) and (3 <= cidx < 6):
                    board_parts["boxs"][1].append(num)
                elif (0 <= ridx < 3) and (6 <= cidx < 9):
                    board_parts["boxs"][2].append(num)
                elif (3 <= ridx < 6) and (0 <= cidx < 3):
                    board_parts["boxs"][3].append(num)
                elif (3 <= ridx < 6) and (3 <= cidx < 6):
                    board_parts["boxs"][4].append(num)
                elif (3 <= ridx < 6) and (6 <= cidx < 9):
                    board_parts["boxs"][5].append(num)
                elif (6 <= ridx < 9) and (0 <= cidx < 3):
                    board_parts["boxs"][6].append(num)
                elif (6 <= ridx < 9) and (3 <= cidx < 6):
                    board_parts["boxs"][7].append(num)
                elif (6 <= ridx < 9) and (6 <= cidx < 9):
                    board_parts["boxs"][8].append(num)

        for row in board_parts["rows"].values():
            if len(row) != len(set(row)):
                return False
        
        for col in board_parts["cols"].values():
            if len(col) != len(set(col)):
                return False

        for box in board_parts["boxs"].values():
            if len(box) != len(set(box)):
                return False

        return True

