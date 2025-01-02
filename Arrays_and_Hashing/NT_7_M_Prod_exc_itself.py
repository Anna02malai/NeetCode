class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res

def main():
    nums = [1,2,4,6]
    res = Solution()
    print(res.productExceptSelf(nums))

if __name__ == "__main__":
    main()