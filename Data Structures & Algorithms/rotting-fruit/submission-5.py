class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n=len(grid), len(grid[0])
        q=deque()
        total, cnt=0,0
        tm=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    total+=1
                if grid[i][j]==2:
                    q.append((i, j))
        
        while q:
            q_len = len(q)
            cnt+=q_len
            for _ in range(q_len):
                i, j = q.popleft()
                for r, c in [(i+1,j), (i-1, j),(i,j+1),(i,j-1)]:
                    if r<0 or r>=m or c<0 or c>=n or grid[r][c]!=1:
                        continue
                    grid[r][c]=2
                    q.append((r,c))
            if q:
                tm+=1
        return tm if cnt==total else -1
            