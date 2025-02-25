class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        
        for i in range(len(nums)):
            res = res ^(i ^ nums[i])
        return res


        # res = len(nums)

        # for i in range(len(nums)):
        #     res += (i - nums[i])
        # return res

def main():
    nums = [1,2,3]
    res = Solution()
    print(res.missingNumber(nums))

if __name__ == "__main__":
    main()    