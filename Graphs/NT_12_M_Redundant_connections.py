class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) +1)
    
        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

def main():
    edges = [[1,2],[1,3],[3,4],[2,4]]
    res = Solution()
    print(res.findRedundantConnection(edges))

if __name__ == "__main__":
    main()                