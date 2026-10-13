class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n=len(board),len(board[0])
        vis=[[0]*n for _ in range(m)]

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or board[i][j]!="O" or vis[i][j]==1:
                return
            vis[i][j]=1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        # boundary check
        for i in range(m):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][n-1]=="O":
                dfs(i,n-1)
        
        for j in range(n):
            if board[0][j]=="O":
                dfs(0,j)
            if board[m-1][j]=="O":
                dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and vis[i][j]!=1:
                    board[i][j]="X"