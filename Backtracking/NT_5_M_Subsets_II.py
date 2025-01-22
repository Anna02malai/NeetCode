class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):

            if i == len(nums):
                res.append(subset[::])
                return
            
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)

        backtrack(0, [])
        return res

def main():
    nums = [1, 2, 1]
    res = Solution()
    print(res.subsetsWithDup(nums))

if __name__ == "__main__":
    main()