class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:

        adjList = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in adjList[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)

def main():
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    res = Solution()
    print(res.validTree(n, edges))

if __name__ == "__main__":
    main()