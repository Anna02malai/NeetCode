class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) in visited):
                return 0
            
            visited.add((r, c))
            return (1 + dfs(r+1, c)
                      + dfs(r-1, c)
                      + dfs(r, c+1)
                      + dfs(r, c-1))
        
        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, dfs(r, c))
        
        return max_area

def main():
    grid = [
            [0,1,1,0,1],
            [1,0,1,0,1],
            [0,1,1,0,1],
            [0,1,0,0,1]
            ]
    res = Solution()
    print(res.maxAreaOfIsland(grid))

if __name__ == "__main__":
    main()