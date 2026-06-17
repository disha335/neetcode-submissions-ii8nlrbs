class Solution:
    def totalNQueens(self, n: int) -> int:
        cnt = 0
        board = [["."]*n for i in range(n)]
        def backtrack(row):
            nonlocal cnt
            if row == n:
                cnt+=1
                return
            for col in range(n):
                if self.isValid(board, row, col):
                    board[row][col]="Q"
                    backtrack(row+1)
                    board[row][col]="."
        backtrack(0)
        return cnt

    def isValid(self, board, row, col):
        # column check
        for x in range(row):
            if board[x][col]=="Q":
                return False
        r, c = row, col
        # Top left
        while r>=0 and c>=0:
            if board[r][c]=="Q":
                return False
            r-=1
            c-=1
        # Top Right
        r, c = row, col
        while r>=0 and c<len(board):
            if board[r][c]=="Q":
                return False
            r-=1
            c+=1
        return True

