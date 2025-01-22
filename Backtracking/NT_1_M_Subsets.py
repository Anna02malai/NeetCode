class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        res, sol = [], []

        def dfs(i):

            if i >= len(nums):
                res.append(sol.copy())
                return
            
            #Decided to Add the Number
            sol.append(nums[i])
            dfs(i + 1)

            #Decided to not add the Number
            sol.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

def main():
    nums = [1,2,3]
    res = Solution()
    print(res.subsets(nums))

if __name__ == "__main__":
    main()