class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen_row_list=[]
        seen_column_list=[[] for _ in range (9)]
        seen_box_list=[[] for _ in range (9)]

        for i in range (0,9):
            del seen_row_list[:]
            for j in range (0,9):
                cell = board[i][j]
                if cell == '.':
                    continue
                if cell in seen_row_list:
                    return False
                    
                seen_row_list.append(cell)

                if cell in seen_column_list[j]:
                    return False
                seen_column_list[j].append(cell)

                box_index= (i//3) * 3 + j // 3
                if cell in seen_box_list[box_index]:
                    return False
                seen_box_list[box_index].append(cell)
        return True
