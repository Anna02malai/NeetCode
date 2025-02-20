from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visited = set()
        total = 0

        while minHeap:
            wt, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            total = wt

            for nd, w in edges[node]:
                if nd not in visited:
                    heapq.heappush(minHeap, (wt + w, nd))
            
        return total if len(visited) == n else -1

def main():
    times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
    n = 4
    k = 1
    res = Solution()
    print(res.networkDelayTime(times, n, k))

if __name__ == "__main__":
    main()