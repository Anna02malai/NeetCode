from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def bfs(r, c):
            if (r<0 or c<0 or r == rows or c == cols or grid[r][c]==-1 or (r, c) in visited):
                return 
            
            q.append([r,c])
            visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r+1, c)
                bfs(r-1, c)
                bfs(r, c+1)
                bfs(r, c-1)
            dist+=1
        return grid

def main():
    grid = [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
            ]
    res = Solution()
    print(res.islandsAndTreasure(grid))

if __name__ == "__main__":
    main()
