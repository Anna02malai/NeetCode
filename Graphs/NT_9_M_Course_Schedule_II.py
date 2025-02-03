class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]):

        preReq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)
        visited, cycle = set(), set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in preReq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return res

def main():
    numCourses = 3
    prerequisites = [[1,0]]
    res = Solution()
    print(res.findOrder(numCourses, prerequisites))

if __name__ == "__main__":
    main()