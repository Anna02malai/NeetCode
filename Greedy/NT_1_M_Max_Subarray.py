class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum <0:
                curSum = 0
            curSum += n
            maxSub = max(curSum, maxSub)
        
        return maxSub

def main():
    nums = [2,-3,4,-2,2,1,-1,4]
    res = Solution()
    print(res.maxSubArray(nums))

if __name__ == "__main__":
    main()