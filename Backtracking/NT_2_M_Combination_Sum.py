class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, curr, total):

            if target == total:
                res.append(curr.copy())
                return
            
            if i>=len(nums) or total>target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i +1, curr, total)
        
        dfs(0, [], 0)
        return res

def main():
    nums = [2,5,6,9]
    target = 9
    res = Solution()
    print(res.combinationSum(nums, target))

if __name__ == "__main__":
    main()