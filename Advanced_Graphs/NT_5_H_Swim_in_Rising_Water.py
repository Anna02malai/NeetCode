import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        minH = [[grid[0][0], 0, 0]] # time/max_height, row, col
        visited = set()
        visited.add((0, 0))
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return t
            
            for dr, dc in directions:
                neiR, neiC = r +dr, c + dc
                if (neiR <0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visited):
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

def main():
    grid = [
            [0,1,2,10],
            [9,14,4,13],
            [12,3,8,15],
            [11,5,7,6]]
    res = Solution()
    print(res.swimInWater(grid))

if __name__ == "__main__":
    main()