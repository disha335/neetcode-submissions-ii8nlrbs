class Solution:
    def isValid(self, board, row, col):
            # Col check
            for x in range(row):
                if board[x][col]=='Q':
                    return False
            # Top Left
            r = row
            c = col
            while r>=0 and c>=0:
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            # Top Right
            r, c = row, col
            while r>=0 and c<len(board):
                if board[r][c]=='Q':
                    return False
                r-=1
                c+=1
            return True
            
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for i in range(n)]
        def backtrack(row):
            if row==n:
                res.append(["".join(row) for row in board])
                return
            for col in range(n):
                if self.isValid(board, row, col):
                    board[row][col]='Q'
                    backtrack(row+1)
                    board[row][col]='.'
        backtrack(0)
        return res