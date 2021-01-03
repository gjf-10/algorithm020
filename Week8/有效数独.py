class Solution:
    def isValidSudoku(self, board) -> bool:
        box_ = [set() for i in range(9)]
        row, col = [set() for i in range(9)],[set() for i in range(9)]
        for i in range(9):
            t = (i // 3) * 3
            for j in range(9):
                index = t + j // 3
                if board[i][j] != '.':
                    if board[i][j] in row[i] or board[i][j] in box_[index] or board[i][j] in col[j]:
                        return False
                    else:
                        row[i].add(board[i][j])
                        box_[index].add(board[i][j])
                        col[j].add(board[i][j])
        return True