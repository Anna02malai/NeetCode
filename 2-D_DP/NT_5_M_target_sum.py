from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                next_dp[curr_sum + num] += count
                next_dp[curr_sum - num] += count
            dp = next_dp
        return dp[target]

def main():
    nums = [2,2,2]
    target = 2
    res = Solution()
    print(res.findTargetSumWays(nums, target))

if __name__ == "__main__":
    main()