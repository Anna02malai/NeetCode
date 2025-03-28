from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)

        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visited = set()
        minH = [[0, 0]]

        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            res += cost
            visited.add(i)

            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, (neiCost, nei))
        return res

def main():
    points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
    res = Solution()
    print(res.minCostConnectPoints(points))

if __name__ == "__main__":
    main()