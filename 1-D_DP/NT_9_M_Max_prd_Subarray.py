class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            tmp = currMax * n
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(tmp, n *currMin, n)
            res = max(res, currMax)
        
        return res

def main():
     nums = [1,2,-3,4]
     res = Solution()
     print(res.maxProduct(nums))

if __name__ == "__main__":
    main()