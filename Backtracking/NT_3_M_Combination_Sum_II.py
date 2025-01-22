class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):

            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr, total)
        
        dfs(0, [], 0)
        return res

def main():
    candidates = [9,2,2,4,6,1,5]
    target = 8
    res = Solution()
    print(res.combinationSum2(candidates, target))

if __name__ == "__main__":
    main()