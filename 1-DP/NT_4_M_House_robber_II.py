class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(self.helper(nums[1:]), self.helper(nums[:-1]), nums[0])

    def helper(self, nums):
        rob1 = 0
        rob2 = 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

def main():
    nums = [2,9,8,3,6]
    res = Solution()
    print(res.rob(nums))

if __name__ == "__main__":
    main()